import sqlite3
import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "todo.db")


class CliTodoList():

    def init():
        conexion = sqlite3.connect(db_path)
        try:
            conexion.execute("""create table todo_list (
                                      id integer primary key autoincrement,
                                      title text not null,
                                      created_at timestamp DEFAULT CURRENT_TIMESTAMP
                                )""")
            conexion.execute("""create table task_list (
                                      id integer primary key autoincrement,
                                      title text not null,
                                      status boolean default True not null,
                                      created_at timestamp  DEFAULT CURRENT_TIMESTAMP,
                                      todo_list_id integer not null
                                )""")
        except sqlite3.OperationalError as e:
            print(e)
            print("database already created")

    def create(title):
        conn = sqlite3.connect(db_path)
        conn.execute(f"""INSERT INTO todo_list (title) VALUES ('{title}')""")
        conn.commit()
        conn.close()

    def update(title, pk):
        conn = sqlite3.connect(db_path)
        conn.execute(f"""UPDATE todo_list SET title='{title}' WHERE id='{pk}';""")
        conn.commit()
        conn.close()

    def delete(name):
        conn = sqlite3.connect(db_path)
        conn.execute(f"""DELETE from todo_list where title={name};""")
        conn.commit()
        conn.close()

    def list():
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.execute("""SELECT id, title, created_at FROM todo_list ORDER BY id DESC""")
            return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def get_by_id(pk):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.execute(f"""SELECT id, title, created_at FROM todo_list WHERE id={pk}""")
            return cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def task_list_by_pk(todo_pk):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.execute(f"""SELECT * FROM task_list WHERE todo_list_id='{todo_pk}'""")
            return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def insert_task(name, todo_pk):
        conn = sqlite3.connect(db_path)
        conn.execute(f"""INSERT INTO task_list (title, todo_list_id) VALUES ('{name}', {todo_pk})""")
        conn.commit()
        conn.close()

    def update_task(title, pk):
        conn = sqlite3.connect(db_path)
        conn.execute(f"""UPDATE task_list SET title='{title}' WHERE id='{pk}';""")
        conn.commit()
        conn.close()

    def change_status_task(pk):
        conn = sqlite3.connect(db_path)
        cursor = conn.execute(f"""SELECT * created_at FROM task_list WHERE id={pk}""")
        row = cursor.fetchone()
        if row is None:
            conn.close()
            return False
        status = True
        if row[2]:
            status = False
        # update
        conn.execute(f"""UPDATE from task_list SET status={status} WHERE id={pk};""")
        conn.commit()
        conn.close()

    def delete_task(pk):
        conn = sqlite3.connect(db_path)
        conn.execute(f"""DELETE from task_list where id={pk};""")
        conn.commit()
        conn.close()
