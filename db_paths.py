from config import username, password, hostname, database

# Databases
path = {
    "scheduler": f"postgresql+psycopg2://{username}:{password}@{hostname}/{database}"
    }
