# python -m venv venv
# .\venv\Scripts\activate
import sqlite3
from sqlite3 import Error
try:
   con = sqlite3.connect("./databases/movies.db")
except Error as e:
    print(e)
