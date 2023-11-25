import requests

def delet_task(task_id):
    # API endpoint to delete a task URL
    delete_task_url = "https://127.0.0.1:5000/tasks/{task_id}"

    # Feth the existing task data
    respnse = requests.get(delete_url)
    existing_task = response.json()
    
    # Display the existing task
    print("Existing Task: ")
    print(existing_task)

    #Prompt user for confirmation
    confirm_deletioin = input("Are you sure you want to delete this task? (y/n): ").lower()

    if confirm_deletioin == "y":
        # Delete the task
        response = requests.delete(delete_url)

        if response.status_code == 200:
            print("Task Deleted")
        else:
            print("Task Deletion Failed")

# Promt the user for a task id to delete
taks_id_to_delete = input("Enter the task ID to delete: ")
delete_taskt(tasks_id_to_delete)