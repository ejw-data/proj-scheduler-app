DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS billing; 
DROP TABLE IF EXISTS calendar; 
DROP TABLE IF EXISTS customers; 
DROP TABLE IF EXISTS events; 
DROP TABLE IF EXISTS organization;
DROP TABLE IF EXISTS subscriptions; 
DROP TABLE IF EXISTS users;

CREATE TABLE organization (
	org_id SERIAL PRIMARY KEY,
	org_name VARCHAR,
	contact_first_name VARCHAR,
	contact_last_name VARCHAR, 
	contact_phone VARCHAR	
);

CREATE TABLE customer (
	cust_id SERIAL PRIMARY KEY,
	org_id INT FOREIGN KEY,
	status VARCHAR
);

CREATE TABLE subscriptions (
	sub_id SERIAL PRIMARY KEY,
	cust_id INT FOREIGN KEY,
	start_date DATE,
	end_date DATE
);

CREATE TABLE users (
	user_id SERIAL PRIMARY KEY,
	sub_id INT FOREIGN KEY,
	account_type VARCHAR
);

CREATE TABLE billing (
	bill_id SERIAL PRIMARY KEY,
	bill_address_1 VARCHAR,
	bill_address_2 VARCHAR,
	bill_city VARCHAR,
	bill_state VARCHAR,
	bill_zipcode VARCHAR,
	bill_frequency VARCHAR
);

CREATE TABLE invoices (
	invoice_id SERIAL PRIMARY KEY,
	bill_id INT FOREIGN KEY,
	sub_id INT FOREIGN KEY,
	price NUMERIC,
	date_billed DATE
	period_start DATE,
	period_end DATE
);

CREATE TABLE receivables (
	receive_id SERIAL PRIMARY KEY,
	invoice_id INT FOREIGN KEY,
	amount_paid NUMERIC,
	date_paid DATE,
	payment_type VARCHAR
);

CREATE TABLE hosts (
	host_id SERIAL PRIMARY KEY,
	sub_id INT FOREIGN KEY,
	host_first_name VARCHAR,
	host_last_name VARCHAR,
	host_email VARCHAR,
	host_phone VARCHAR,
	host_permission_group VARCHAR	
);

CREATE TABLE appointments (
	event_id SERIAL PRIMARY KEY,
	user_id INT FOREIGN KEY,
	host_id INT	FOREIGN KEY
);