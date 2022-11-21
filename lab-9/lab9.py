import sqlite3

from sqlite3 import Error

# Функція для створення з'єднання до БД 
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


# Вибір всіх значень в таблиці tasks
def select_all_tasks(conn):
    sql = 'SELECT id,name FROM data'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


# Створення нового завдання
def create_task(conn, task):
    sql = ''' INSERT INTO data(id,name)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)


# Оновлення дати в завданні
def update_data_task(conn, data):
    sql = ''' UPDATE data
              SET name = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    

# Видалення завдання за його текстом
def remove_task(conn, removed_task):
    sql = ''' DELETE FROM data WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, removed_task)
    conn.commit()


# Головна функція, яка виконується під час запуску скрипта
def main():

#     # Шлях до БД
    database = r"new.db" 
 
#     # Встановлення з'єднання
    conn = create_connection(database)

    # Використовууючи встановлене з'єднання виконуються операції над БД
    with conn:
        print("\nВсі завдання (завдання)")
        select_all_tasks(conn)
        input("Натисніть ENTER, щоб продовжити...\n")

        print("\nВставка нового рядка...")
        create_task(conn, ('4','Complete the task'))
        print("\nВсі завдання (завдання)")
        select_all_tasks(conn)
        input("Натисніть ENTER, щоб продовжити...\n")

        print("\nЗміна рядка...")
        update_data_task(conn, ('Task completed','4'))
        print("\nВсі завдання (завдання)")
        select_all_tasks(conn)        
        input("Натисніть ENTER, щоб продовжити...\n")

        print("\nВидалення рядка")
        remove_task(conn, '4')
        print("\nВсі завдання (завдання)")
        select_all_tasks(conn)
        input("Натисніть ENTER, щоб продовжити...\n")
        
 
if __name__ == '__main__':
    main()
