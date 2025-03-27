import sqlite3

def create_connection(db_name):
    connection = None

    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as k:
        print(k)
        return connection
sql_to_create_categories_table = '''
CREATE TABLE categories (
    code VARCHAR(2) PRIMARY KEY NOT NULL,
    title VARCHAR(150) NOT NULL 
)
'''
def insert_categories(connection, categories):
    sql = '''
    INSERT INTO categories (code, title)
    VALUES (?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, categories)
        connection.commit()
    except sqlite3.Error as k:
        print(k)

database_name = 'PRACTICAL_EXAM.db'
my_connection = create_connection(database_name)
if my_connection is not None:
    print('Connected')
insert_categories(my_connection, ('FD', 'Food Products'))
insert_categories(my_connection, ('EL', 'Electronics'))
insert_categories(my_connection, ('CL', 'Closes'))




my_connection.close()