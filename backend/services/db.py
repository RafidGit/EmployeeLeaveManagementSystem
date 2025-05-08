import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="sheraspacetest",
        user="postgres",
        password="1234"
    )
