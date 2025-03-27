import sqlite3

def setup_database():
    conn = sqlite3.connect("exams.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        code VARCHAR(2) PRIMARY KEY NOT NULL,
        title VARCHAR(150) NOT NULL
    )''')


    cursor.executemany('INSERT OR IGNORE INTO categories (code, title) VALUES (?, ?)', [
        ('FD', 'Food Products'),
        ('EL', 'Electronics'),
        ('CL', 'Clothes')
    ])

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stores (
        store_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(100) NOT NULL
    )''')

    cursor.executemany('INSERT OR IGNORE INTO stores (store_id, title) VALUES (?, ?)', [
        (1, 'Asia'),
        (2, 'Globus'),
        (3, 'Spar')
    ])

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category_code VARCHAR(2),
        unit_price FLOAT,
        stock_quantity INTEGER,
        store_id INTEGER,
        FOREIGN KEY (category_code) REFERENCES categories(code),
        FOREIGN KEY (store_id) REFERENCES stores(store_id)
    )''')

    cursor.executemany('INSERT INTO products (title, category_code, unit_price, stock_quantity, store_id) VALUES (?, ?, ?, ?, ?)', [
        ('Chocolate', 'FD', 10.5, 129, 1),
        ('Jeans', 'CL', 120.0, 55, 2),
        ('T-Shirt', 'CL', 0.0, 15, 1)
    ])

    conn.commit()
    conn.close()

def display_supermarket():
    conn = sqlite3.connect("exams.db")
    cursor = conn.cursor()

    cursor.execute("SELECT store_id, title FROM stores")
    stores = cursor.fetchall()

    print("Список магазинов:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")

    print("\nВведите ID магазина, чтобы посмотреть доступные товары. Для выхода введите 0.")

    while True:
        store_id = input("Введите ID магазина: ")
        if store_id == "0":
            print("Выход из программы.")
            break

        try:
            store_id = int(store_id)
            cursor.execute("SELECT title, unit_price, stock_quantity FROM products WHERE store_id = ?", (store_id,))
            products = cursor.fetchall()

            if products:
                print(f"\nТовары в магазине с ID {store_id}:")
                for product in products:
                    print(f"{product[0]} - {product[1]}сом (В наличии: {product[2]} шт.)")
            else:
                print("В этом магазине пока нет товаров.")

        except ValueError:
            print("Ошибка! Введите корректное число.")

    conn.close()

if __name__ == "__main__":
    setup_database()
    display_supermarket()
