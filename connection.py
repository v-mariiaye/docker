import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Підключення до бази даних PostgreSQL пройшло успішно")

    except OperationalError as e:
        print(f"Произошла ошибка '{e}'")
    return connection



def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Запит успішно опрацьований")
    except OperationalError as e:
        print(f"Помилка '{e}'")