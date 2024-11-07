#1 luo yhteys movies.bd tiedostoon
#2 hae 10 ensimaista elokuvaa
#3 kirjoita tulokset csv tiedostoon
import sqlite_connection as db
import pandas as pd
from pathlib import Path
import sqlite3

#create empty file
Path('leffat.db').touch()

#create connection
con = sqlite3.connect("./databases/leffat.db")
connection = db.con

#create db cursor
cursor = connection.cursor()
table_mane = "movies"
cursor.execute("CREATE TABLE IF NOT EXISTS movies(id INT, \
                title TEXT, \
            overview TEXT, \
            popularity REAL, \
            release_date TEXT, \
            vote_average REAL, \
            vote_count INT)")
column_names = ["id", "title", "overview", "popularity", "release_date", "vote_average", "vote_count"]
movie_data = pd.read_csv('leffat.csv', delimiter=';', names=column_names)
# Define correct column names as per the database table schema
print(movie_data.head(5))

movie_data.to_sql('movies', connection, if_exists='append', index=False)

connection.close()