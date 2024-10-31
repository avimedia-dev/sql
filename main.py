import sqlite_connection as db
import json
import pandas as pd

with db.con as connection:

    #cur = connection.execute("SELECT \
    #                        * \
    #                        FROM movies  \
    #                        WHERE title == 'Oppenheimer'")
    cur = connection.execute("SELECT \
                            * \
                            FROM movies")
    #for row in rows:
    #   print(row)
    #result = ""
    #while result != None: 
        #result = cur.fetchone()
        #print(result)
    iterator = iter(cur)
    line = next(iterator)
    with open("movies_list.csv", "w") as movies_file:
        for item in line:
            movies_file.write(str(item)+";")
        json_dump = json.dumps(line)
        with open("movies_json.json", "w") as movies_json:
            movies_json.write(json_dump)
        df = pd.DataFrame(line)
        df.head(5)
        df.to_csv("pandas_csv.csv", index=True, sep=";")
        print("dataframe:", df)
    #line2 = next(iterator)
    print(line)
    list = cur.fetchall()
    df = pd.DataFrame(list)

    df.to_csv("leffat.csv", index=False, sep=";")
connection.close()


