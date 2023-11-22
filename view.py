from tabulate import tabulate

def displaying_table(cur):
    # Отримання списку всіх таблиць у базі даних
    cur.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    """)
    tables = [table[0] for table in cur.fetchall()]

    # Виведення структури та даних для кожної таблиці
    for table_name in tables:
        print(f"Таблиця: {table_name}")
        cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'")
        columns = cur.fetchall()
        print(tabulate(columns, headers=["Назва стовпця", "Тип даних"], tablefmt="pretty"))

        cur.execute(f'SELECT * FROM "{table_name}"')
        data = cur.fetchall()
        print(tabulate(data, headers=[column[0] for column in cur.description], tablefmt="pretty"))
        print("\n")


