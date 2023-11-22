import random
from tables import*
from faker import Faker
from datetime import date

fake = Faker('uk_UA')

def write(cursor):
    error_levels = ['критична', 'важлива', 'незначна']
    func_categories = ['інтерфейс', 'дані', 'розрахунковий алгоритм', 'інше', 'невідома категорія']
    sources = ['користувач', 'тестувальник']

    # Заповнення таблиці "Помилки" даними
    for _ in range(20):
        cursor.execute("""
                INSERT INTO "Error" (Description, Date_receipt, Error_level, Func_category, Source)
                VALUES (%s, %s, %s, %s, %s)
            """, (
            fake.text(),
            fake.date_this_year(),
            random.choice(error_levels),
            random.choice(func_categories),
            random.choice(sources)
        ))

    # Заповнення таблиці "Програмісти, відповідальні за виправлення помилки" даними
    for _ in range(4):
        cursor.execute("""
                INSERT INTO "Resp_programmers" (Surname, Name, Phone_number)
                VALUES (%s, %s, %s)
            """, (
            fake.last_name(),
            fake.first_name(),
            fake.phone_number()
        ))

    # Заповнення таблиці "Виправлення помилок" даними
    correction_start_dates = [fake.date_this_year() for _ in range(20)]
    term_correction_values = [1, 2, 3]
    cost_of_work_values = [100, 150, 200]

    for i in range(20):
        cursor.execute("""
                INSERT INTO "Correction_errors" (ID_error, ID_programmer, Correction_start_date, Term_correction, Cost_of_work_1_day_prog)
                VALUES (%s, %s, %s, %s, %s)
            """, (
            i + 1,  # Припускаючи, що ідентифікатори помилок починаються з 1
            random.randint(1, 4),  # Припускаючи, що є 4 програмісти
            correction_start_dates[i],
            random.choice(term_correction_values),
            random.choice(cost_of_work_values)
        ))