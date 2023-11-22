from connection import *
from tables import *
from view import displaying_table
from db import write
from request import *

connection = create_connection(
    "postgres", "admin", "root", "127.0.0.1", "5432"
)

execute_query(connection, create_error_table)
execute_query(connection, create_programmers_table)
execute_query(connection, create_correction_table)

cursor = connection.cursor()
cur = connection.cursor()

#write(cursor)
#print_data(cursor)
displaying_table(cur)
