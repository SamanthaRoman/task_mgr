from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        res = {
            "id": result[0],
            "summary": result[1],
            "description": result[2],
            "is_done": result[3]
        }
        out.append(res)
    return out

def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE is_done=0", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def select_by_id(task_id):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE id=?", (task_id, )) # comma! ## passing data to the question mark
    results = cursor.fetchall()
    cursor.close()
    if results:
        return output_formatter(results)[0]
    return {}

def insert(task_data):
    conn = get_db()
    task_tuple = (      
        task_data.get("summary"),
        task_data.get("description")
    )
    statement = """
        INSERT INTO task (
            summary,
            description
        ) VALUES (?, ?)
    """
    conn.execute(statement, task_tuple)
    conn.commit()

def update_by_id(task_data, task_id):
    conn = get_db()
    task_tuple = (      # purpose to map into statement.
        task_data.get("summary"),
        task_data.get("description"),
        task_data.get("is_done"),
        task_id
    )
    statement = """
        UPDATE task SET
            summary = ?,
            description = ?,
            is_done = ?
        WHERE id = ?
    """

    conn.execute(statement, task_tuple)
    conn.commit()

    def delete_by_id(task_id):
        conn = get_db()
        conn.execute("DELETE FROM task WHERE id=?", (task_id, )) # comma
        conn.commit()
