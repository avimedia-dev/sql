import sqlite3

conn = sqlite3.connect("../databases/albums.db")
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS albums (id integer primary key \
        , artist_name text \
        , album_name text \
        ,year text \
        , genre text)"
)
conn.commit() # ilman tätä ei tallenna lisäystä ohjelman sulkeutuessa

def add_album(artist, album, year, genre):
    ##LISÄÄ INSERT-LAUSE,JOKA LISÄÄ TIETOKANTAAN ANNETUT TIEDOT OMAKSI RIVIKSEEN
    insert_data = ("""INSERT INTO albums (id, artist_name,album_name,year,genre)
                        VALUES(NULL,?,?,?,?)
                   """)
    cursor.execute(insert_data, (artist, album, year, genre))
    conn.commit() # ilman tätä ei tallenna lisäystä ohjelman sulkeutuessa


def fetch_albums():
    cursor.execute("SELECT * FROM albums")    
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(
            str(row[0])
            + "-"
            + str(row[1])
            + "-"
            + row[2]
            + "-"
            + row[3]
            + "-"
            + str(row[4])
        )
    return result


def remove(selected_album):
    #LISÄÄ DELETE-LAUSEKE->POISTETAAN ID:N MUKAAN RIVI (ID:N SAA SELVILLE parameterina tullesta selected_album:ista!)
    print(selected_album)
    remove_data = ("DELETE FROM albums WHERE id = ?")
    cursor.execute(remove_data, (selected_album[0],))
    conn.commit()


def update(selected_album, artist, album, year, genre):
    #LISÄÄ UPDATE-LAUSE, JOKA PÄIVITÄÄ RIVIN ID:n MUKAAN (ID:N SAA SELVILLE parameterina tullesta selected_album:ista)
    update_data = ("UPDATE albums SET artist_name = ?, album_name = ?, year = ?, genre = ? WHERE id = ?")
    cursor.execute(update_data, (artist, album, year, genre, selected_album[0] ))
    conn.commit()


def __del__():  # destructor call when all instances of object has been deleted
    print("__del__ called")
    conn.close()
