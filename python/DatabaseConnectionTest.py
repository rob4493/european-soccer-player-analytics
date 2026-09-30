import os

import psycopg
from dotenv import load_dotenv


load_dotenv()

DbHost = os.getenv("DBHOST")
DbPort = os.getenv("DBPORT")
DbName = os.getenv("DBNAME")
DbUser = os.getenv("DBUSER")
DbPassword = os.getenv("DBPASSWORD")


Connection = psycopg.connect(
    host=DbHost,
    port=DbPort,
    dbname=DbName,
    user=DbUser,
    password=DbPassword
)

print("Python successfully connected to PostgreSQL.")


Cursor = Connection.cursor()

Cursor.execute("SELECT current_database();")

Result = Cursor.fetchone()

print("Connected database:", Result[0])


Cursor.close()
Connection.close()

print("Database connection closed successfully.")