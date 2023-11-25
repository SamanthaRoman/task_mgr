import requests         # requests tool we installed.

BACKEND_URL = "http://127.0.0.1:5000/tasks"

def create_task(summary, description):
    raw_task = {
        "summary": summary,
        "description": description
    }
    response = requests.post(BACKEND_URL, json=raw_task)    #convert to json using key work
    if response.status_code == 201:                         #keyword argument is equal signs
        print("Creations succeeded.")   #this could be an entire web that says success or w.e. you want
    else:
        print("Creation failed.")


if __name__ == "__main__":
    print("Create a task by following the prompts below:")
    summary = input("Summary: ")
    description = input("Description: ")
    create_task(summary, description)