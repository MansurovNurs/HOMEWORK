import sqlite3


def setup_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )''')

    cursor.executemany('INSERT INTO countries (title) VALUES (?)', [
        ('Кыргызстан',), ('Германия',), ('Китай',)
    ])

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )''')

    cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', [
        ('Бишкек', 160, 1), ('Ош', 182, 1),
        ('Берлин', 891.8, 2), ('Мюнхен', 310.7, 2),
        ('Пекин', 16410, 3), ('Шанхай', 6340, 3), ('Гуанчжоу', 7434, 3)
    ])

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    )''')

    cursor.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)', [
        ('Иван', 'Петров', 1), ('Анна', 'Сидорова', 1), ('Борис', 'Иванов', 1),
        ('Фатима', 'Ахмедова', 2), ('Жан', 'Ким', 2),
        ('Ганс', 'Мюллер', 3), ('Катарина', 'Шмидт', 3),
        ('Лукас', 'Вагнер', 4), ('Леони', 'Беккер', 4),
        ('Вэй', 'Чжан', 5), ('Мин', 'Ли', 5),
        ('Цзяо', 'Хуанг', 6), ('Юань', 'Дэн', 6),
        ('Лэй', 'Ву', 7), ('Янь', 'Чэнь', 7)
    ])

    conn.commit()
    conn.close()


def display_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()

    print("Выберите город по ID или введите 0 для выхода:")
    for city in cities:
        print(f"{city[0]}. {city[1]}")

    while True:
        city_id = input("Введите ID города: ")
        if city_id == "0":
            break

        cursor.execute('''
        SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
        FROM students
        JOIN cities ON students.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
        ''', (city_id,))

        students = cursor.fetchall()

        if students:
            print("\nУченики в этом городе:")
            for student in students:
                print(f"{student[0]} {student[1]}, {student[2]}, {student[3]}, Площадь: {student[4]} кв.км")
        else:
            print("\nВ этом городе нет учеников.")

    conn.close()


if __name__ == "__main__":
    setup_database()
    display_students()
