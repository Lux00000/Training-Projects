import psycopg2

conn = psycopg2.connect(database = "niceone", user = 'postgres', host = "localhost", port = '5432', password = '12345')

def create_employee_table():
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                gender VARCHAR(10)
            )
        """)
        conn.commit()
        print("Successfull")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Create Error", error)


def insert_employee_data(first_name, last_name, gender):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO employee (first_name, last_name, gender)
            VALUES (%s, %s, %s)
        """, (first_name, last_name, gender))
        conn.commit()
        print("Данные успешно добавлены в таблицу 'employee'.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при добавлении данных в таблицу 'employee':", error)

# Редактирование данных в таблице "employee"
def update_employee_data(employee_id, first_name, last_name, gender):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE employee
            SET first_name = %s, last_name = %s, gender = %s
            WHERE id = %s
        """, (first_name, last_name, gender, employee_id))
        conn.commit()
        print("Update!")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Update Error", error)
