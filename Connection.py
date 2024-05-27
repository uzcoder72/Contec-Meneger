import psycopg2
def get_database_connection():
    try:
        db_name = 'n47'
        password = '123'
        host = 'localhost'
        port = 5432
        user = 'postgres'

        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None
if __name__ == "__main__":
    connection = get_database_connection()
    if connection:
        print("Connected successfully!")
        connection.close()
    else:
        print("Failed to connect to the database.")
class DatabaseContextManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def __enter__(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM products")
        result = cursor.fetchall()
        return result

    def __exit__(self, exc_type, exc_value, traceback):
        self.db_connection.close()

db_connection = get_database_connection()
with DatabaseContextManager(db_connection) as data:
    for row in data:
        print(row)