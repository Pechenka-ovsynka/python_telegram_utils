import sqlite3

def run_bd():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        #print("База данных создана и успешно подключена к SQLite")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        #print("Версия базы данных SQLite: ", record)
        cursor.close()
    except sqlite3.Error as error:
        #print("Ошибка при подключении к sqlite", error)
        pass
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        sqlite_create_table_query = '''CREATE TABLE sending_message (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    user_id INTEGER NOT NULL UNIQUE,
                                    sending bool default 0);'''
        cursor = sqlite_connection.cursor()
        #print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        #print("Таблица SQLite создана")
        cursor.close()

    except sqlite3.Error as error:
        #print("Ошибка при подключении к sqlite", error)
        pass
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            #print("Соединение с SQLite закрыто")


def insert_bd(user_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()

        sqlite_insert_query = f"""INSERT INTO sending_message
                              (user_id)  VALUES  ( '{user_id}')"""
        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        #print(error)
        pass
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def sucs_bd(user_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        sqlite_insert_query = f"""update sending_message
                              set sending=1 where user_id= {user_id}"""

        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        #print(error)
        pass
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def is_send(user_id):
    total_rows=""
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        sqlite_select_query = f"""SELECT sending from sending_message where user_id= {user_id}"""
        cursor.execute(sqlite_select_query)
        total_rows = cursor.fetchone()
        cursor.close()

    except sqlite3.Error as error:
        #print(error)
        pass
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    #print(total_rows[0])
    return total_rows[0]