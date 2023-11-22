from tabulate import tabulate

def print_data(cursor):
    # Запит: Відобразити всі критичні помилки. Відсортувати по коду помилки.
    cursor.execute("""
        SELECT *
        FROM "Error"
        WHERE Error_level = 'критична'
        ORDER BY ID_error;
    """)
    result = cursor.fetchall()
    print("\nКритичні помилки:")
    print(tabulate(result, headers=[desc[0] for desc in cursor.description], tablefmt="pretty"))

    # Запит: Порахувати кількість помилок кожного рівня (підсумковий запит)
    cursor.execute("""
        SELECT Error_level, COUNT(*) as Count_errors
        FROM "Error"
        GROUP BY Error_level;
    """)
    result = cursor.fetchall()
    print("\nКількість помилок кожного рівня:")
    print(tabulate(result, headers=["Error Level", "Count"], tablefmt="pretty"))

    # Запит: Порахувати вартість роботи програміста при виправленні кожної помилки (з обчислювальним полем)
    cursor.execute("""
        SELECT
            ce.ID_error,
            ce.ID_programmer,
            ce.Cost_of_work_1_day_prog * ce.Term_correction as Total_cost
        FROM "Correction_errors" ce;
    """)
    result = cursor.fetchall()
    print("\nВартість роботи програміста при виправленні кожної помилки:")
    print(tabulate(result, headers=["ID_error", "ID_programmer", "Total_cost"], tablefmt="pretty"))

    # Запит: Відобразити всі помилки, які надійшли із заданого джерела (запит з параметром)
    source_to_display = 'користувач'
    cursor.execute("""
        SELECT *
        FROM "Error"
        WHERE Source = %s;
    """, (source_to_display,))
    result = cursor.fetchall()
    print(f"\nПомилки, надійшли із джерела '{source_to_display}':")
    print(tabulate(result, headers=[desc[0] for desc in cursor.description], tablefmt="pretty"))

    # Запит: Порахувати кількість помилок, які надійшли від користувачів, та тестувальників (підсумковий запит)
    cursor.execute("""
        SELECT Source, COUNT(*) as Count_errors
        FROM "Error"
        WHERE Source IN ('користувач', 'тестувальник')
        GROUP BY Source;
    """)
    result = cursor.fetchall()
    print("\nКількість помилок, надійшли від користувачів та тестувальників:")
    print(tabulate(result, headers=["Source", "Count_errors"], tablefmt="pretty"))

    # Запит: Порахувати кількість критичних, важливих, незначних помилок, виправлених кожним програмістом (перехресний запит)
    cursor.execute("""
        SELECT
            rp.Surname,
            rp.Name,
            COUNT(*) as Count_critical,
            SUM(CASE WHEN e.Error_level = 'важлива' THEN 1 ELSE 0 END) as Count_major,
            SUM(CASE WHEN e.Error_level = 'незначна' THEN 1 ELSE 0 END) as Count_minor
        FROM "Resp_programmers" rp
        JOIN "Correction_errors" ce ON rp.ID_programmer = ce.ID_programmer
        JOIN "Error" e ON ce.ID_error = e.ID_error
        WHERE e.Error_level = 'критична'
        GROUP BY rp.Surname, rp.Name;
    """)
    result = cursor.fetchall()
    print("\nКількість критичних, важливих, незначних помилок, виправлених кожним програмістом:")
    print(tabulate(result, headers=["Surname", "Name", "Count_critical", "Count_major", "Count_minor"], tablefmt="pretty"))

