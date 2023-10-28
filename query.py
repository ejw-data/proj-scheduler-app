from sqlalchemy import create_engine


def submission_request():
    '''
    App login
    '''

    engine = create_engine('sqlite:///gradebook.db')

    query = '''
    With studentCTE(student_id, person_id,sCTEcohort_id) AS 
        (SELECT student_id, person_id, cohort_id
        FROM student s 
        WHERE cohort_id = 
            (SELECT c.cohort_id 
            FROM cohort c 
            WHERE DATE() > c.start_date
            AND DATE() < c.end_date
            )
        ), 
    unitCTE (unit_id, uCTEcohort_id, unit_due) AS 
        (SELECT unit_id, cohort_id, unit_due
        FROM unit u
        WHERE cohort_id = 
            (SELECT c.cohort_id 
            FROM cohort c 
            WHERE DATE() > c.start_date
            AND DATE() < c.end_date
            )
        AND unit_required = 1
        AND unit_due < DATE()
        )
    SELECT sb.unit_id, 
        COUNT(1) FILTER(WHERE label = "Very Early") as VeryEarly,
        COUNT(1) FILTER(WHERE label = "Early") as Early,
        COUNT(1) FILTER(WHERE label = "On-time") as Ontime, 
        COUNT(1) FILTER(WHERE label = "Late") as Late, 
        COUNT(1) FILTER(WHERE label = "Very Late") as VeryLate, 
        COUNT(1) FILTER(WHERE label IS NULL) as NU
    FROM submission sb
    INNER JOIN studentCTE 
    ON sb.student_id = studentCTE.student_id
    INNER JOIN unitCTE
    ON sb.unit_id = unitCTE.unit_id  
    LEFT JOIN (
    SELECT attendance_status.*, lead(bin) OVER (ORDER BY bin NULLS FIRST) AS next_bin
    from attendance_status
    ) b ON (bin IS NULL OR ROUND(JULIANDAY(sb.submission_date) - JULIANDAY(unitCTE.unit_due)) >= bin) AND (next_bin IS NULL OR ROUND(JULIANDAY(sb.submission_date) - JULIANDAY(unitCTE.unit_due)) < next_bin)
    GROUP BY sb.unit_id;
    '''

    conn = engine.connect()

    data = conn.execute(query).fetchall()

    unit, veryearly, early, ontime, late, verylate, ns = [], [], [], [], [], [], []

    for row in data:
        unit.append(row[0])
        veryearly.append(row[1])
        early.append(row[2])
        ontime.append(row[3])
        late.append(row[4])
        verylate.append(row[5])
        ns.append(row[6])

    submission_dict = {
        "unit": unit,
        "veryearly": veryearly,
        "early": early,
        "ontime": ontime,
        "late": late,
        "verylate": verylate,
        "notsubmitted": ns
    }  

    conn.close()
    engine.dispose()

    return submission_dict
