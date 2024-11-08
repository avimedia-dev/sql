#pip install flask
#flask run --debug
from mysql_connection import create_connection

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

conn = create_connection()

if conn:
    cursor = conn.cursor()
    table_name = "tasks"
    cursor.execute(f"USE task_db")
    #cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, task VARCHAR(255), status BOOLEAN)"
    print("SQL Query:", create_table_query)
    cursor.execute(create_table_query)
    conn.commit()

@app.route('/')
def home():
    all_tasks_query = f"SELECT * FROM {table_name}"
    cursor.execute(all_tasks_query)
    tasks = cursor.fetchall()
    return render_template('index.html', all_tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    print(task)
    add_task_query = f"INSERT INTO {table_name} (task, status) VALUES (%s, %s)"
    print(add_task_query)
    cursor.execute(add_task_query, (task, False))
    conn.commit()   
    return redirect('/')

@app.route('/edit/<int:task_id>', methods=['PUT'])
def edit_task(task_id):
    print(task_id)
    edit_task_query = f"DELETE FROM {table_name} WHERE id = %s"
    print(edit_task_query)
    cursor.execute(edit_task_query, (task_id,))
    conn.commit()   
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    print(task_id)
    delete_task_query = f"DELETE FROM {table_name} WHERE id = %s"
    print(delete_task_query)
    cursor.execute(delete_task_query, [task_id])
    conn.commit()   
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)