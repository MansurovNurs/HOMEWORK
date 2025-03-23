import sqlite3

# def create_connection(db_name):
#     connection = None
#
#     try:
#         connection = sqlite3.connect(db_name)
#     except sqlite3.Error as k:
#         print(k)
#         return connection

# def create_table(connection, create_table_sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(create_table_sql)
#     except sqlite3.Error as k:
#         print(k)

def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as k:
        print(k)

def insert_product(connection, product):
    sql = '''
    INSERT INTO products(product_title, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as k:
        print(k)

def update_product(connection, product):
    sql = '''
    UPDATE products SET price = ? WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as k:
        print(k)

def delete_product(connection, id):
    sql = '''
    DELETE FROM products WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as k:
        print(k)

def update_product(connection, product):
    sql = '''
    UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as k:
        print(k)

def select_all_products(db_name):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute('')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as k:
        print(k)

def select_products_by_price(db_name, price_limit, quantity_limit):
    sql = '''SELECT id, price, quantity FROM products WHERE price <= ? and quantity <= ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as k:
        print(k)

sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0,0,
    quantity INTEGER NOT NULL QUANTITY 0)
'''

database_name = 'HW.db'
my_connection = create_connection(database_name)
if my_connection is not None:
    print('Connected')
    create_table(my_connection, sql_to_create_products_table)
    # insert_product(my_connection, ('POTATOES', 65, 10))
    #
    # insert_product(my_connection, ('ONION', 45, 8))
    # insert_product(my_connection, ('CARROT', 35, 6))
    # insert_product(my_connection, ('CUCUMBER', 75, 3))
    # insert_product(my_connection, ('MELON', 100, 2))
    # insert_product(my_connection, ('WATERMELON', 90, 4))
    # insert_product(my_connection, ('GARLIC', 25, 15))
    # insert_product(my_connection, ('APPLE', 30, 5))
    # insert_product(my_connection, ('PEACH', 50, 6))
    # insert_product(my_connection, ('GRAPES', 70, 6))
    # insert_product(my_connection, ('CHERRY', 86, 3))
    # insert_product(my_connection, ('BERRY', 75, 9))
    # insert_product(my_connection, ('BLUEBERRY', 95, 1))
    # insert_product(my_connection, ('PINEAPPLE', 67, 6))
    # insert_product(my_connection, ('RASPBERRY', 45, 9))
    update_product(database_name, (55, 3))
    update_product(database_name, (12, 5))
    delete_product(database_name, 6)
    select_products_by_price(database_name, 50, 4)



    my_connection.close()

