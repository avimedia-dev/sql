import sqlite3
from sqlite3 import Error

import os
db_path = "../databases/employees.db"

def connect_to_db(filename):
    if not os.path.isfile(filename):
        print(f"Database file '{filename}' does not exist and it will be created.")
    return sqlite3.connect(filename)

try:
    conn = connect_to_db(db_path)
    if conn is None:
       print("no connection")
    else:
        print("connection ok")
except Error as e:
    print(e)
    conn = None

