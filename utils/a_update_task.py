import requests

BACKEND_URL = "http://127.0.0.1:5000/tasks"

def update_task(summary, description, task_id):
    update_task = {
        "summary": summary,
        "description": description,
        "is done": 0
    }
    response = requests.put(f"{BACKEND_URL}/{task_id}", json=update_task) 
    if response.status_code == 204:
        print("Update Succes")
    else:
        print("Update failed ")


if __name__ == "__main__":
    print("To update task follow the responses")
    summary = input("Summary: ")
    description = input("Description: ")
    task_id = input("Task ID: ")
    update_task(summary, description, task_id)