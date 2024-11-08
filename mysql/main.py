from mysql_connection import create_connection
import pandas as pd
from sqlalchemy import create_engine

conn = create_connection()
csv_file_path = "../databases/us-500.csv"
df = pd.read_csv(csv_file_path)
print(df.head(5))
#df.to_sql("employees", conn, if_exists="replace", index=True)
# result_df = pd.read_sql("SELECT * FROM employees", conn)
# print(result_df.head(5))
if conn:
    cursor = conn.cursor()
    table_name = "all_employees"
    column_names = df.columns.tolist()

    column_types = ['id INT AUTO_INCREMENT PRIMARY KEY'] #to add index !!! different for mysql
    for column in df.columns:
        if pd.api.types.is_integer_dtype(df[column]):
            column_type = "INTEGER"
        elif pd.api.types.is_float_dtype(df[column]):
            column_type = "REAL"
        else:
            column_type = "TEXT"
        column_types.append(f"{column} {column_type}")
    cursor.execute(f"USE kayttajat")
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_types)})"
    print("SQL Query:", create_table_query)

    cursor.execute(create_table_query)
    data_tuples = [tuple(x) for x in df.to_numpy()] #to_numpy converts dataframe to array
    insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s' for _ in df.columns])})"
    print(insert_query)
    cursor.executemany(insert_query, data_tuples)
    conn.commit()

    #Warning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
    #pip install SQLAlchemy
    username = 'alex'
    password = '1'
    host = 'localhost'
    database = 'kayttajat'

    # Create the SQLAlchemy engine
    engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}/{database}")

    result_df = pd.read_sql(f"SELECT * FROM {table_name}", engine)
    print(result_df.head())   


if conn:
    conn.close()