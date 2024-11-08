#pip install pymysql 
import pymysql

try:
    conn = pymysql.connect(
        host='localhost',
        user='alex',
        password='1',
        database='kayttajat' 
    )
    conn.close()
    print("OK")
except:
    print("CONNECTION FAILED")