# Створення таблиці "Помилки"
create_error_table= ("""
    CREATE TABLE IF NOT EXISTS "Error" (
    ID_error SERIAL PRIMARY KEY,
    Description VARCHAR(255),
    Date_receipt DATE,
    Error_level VARCHAR(50) CHECK (Error_level IN ('критична', 'важлива', 'незначна')),
    Func_category VARCHAR(50) CHECK (Func_category IN ('інтерфейс', 'дані', 'розрахунковий алгоритм', 'інше', 'невідома категорія')),
    Source VARCHAR(50) CHECK (Source IN ('користувач', 'тестувальник'))
    )
""")

# Створення таблиці "Програмісти, відповідальні за виправлення помилки"
create_programmers_table= ("""
    CREATE TABLE IF NOT EXISTS "Resp_programmers" (
    ID_programmer SERIAL PRIMARY KEY,
    Surname VARCHAR(50),
    Name VARCHAR(50),
    Phone_number VARCHAR(25)
)
""")

# Створення таблиці "Виправлення помилок"
create_correction_table= ("""
    CREATE TABLE IF NOT EXISTS "Correction_errors" (
    ID_correction SERIAL PRIMARY KEY,
    ID_error INTEGER REFERENCES "Error" (ID_error),
    ID_programmer INTEGER REFERENCES "Resp_programmers" (ID_programmer),
    Correction_start_date DATE,
    Term_correction INTEGER CHECK (Term_correction IN (1, 2, 3)),
    Cost_of_work_1_day_prog INTEGER
    )
""")
