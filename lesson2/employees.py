import sqlite_connection as db
import pandas as pd
from faker import Faker

csv_file_path = "../databases/us-500.csv"
with db.conn as connection:
    df = pd.read_csv(csv_file_path)
    #print(df.head(5))
    #how to create database by pandas
    df.to_sql("employees", connection, if_exists="replace", index=True)
    result_df = pd.read_sql("SELECT * FROM employees", connection)
    print(result_df.head(5))
    #how to create database by sqlite and sql query
    cursor = connection.cursor()
    table_name = "all_employees"
    column_names = df.columns.tolist()

    column_types = ['id INTEGER PRIMARY KEY AUTOINCREMENT'] #to add index
    for column in df.columns:
        if pd.api.types.is_integer_dtype(df[column]):
            column_type = "INTEGER"
        elif pd.api.types.is_float_dtype(df[column]):
            column_type = "REAL"
        else:
            column_type = "TEXT"
        column_types.append(f"{column} {column_type}")

    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_types)})"
    print("SQL Query:", create_table_query)

    cursor.execute(create_table_query)
    data_tuples = [tuple(x) for x in df.to_numpy()]
    insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['?' for _ in df.columns])})"
    cursor.executemany(insert_query, data_tuples)

    result_df = pd.read_sql(f"SELECT * FROM {table_name}", connection)
    print(result_df.head())   

    connection.commit()

    fake = Faker()
    print(fake.name())




