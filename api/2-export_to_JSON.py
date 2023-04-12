#!/usr/bin/python3
"""Using what you did in the task #0
 extend your Python script
 to export data in the JSON format."""
import json
import requests
import sys
if __name__ == '__main__':
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(id)).json()
    tasks = []
    for task in todos:
        task_dict = {}
        task_dict["title"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = users.get("username")
        tasks.append(task_dict)
    data = {}
    data[id] = tasks
    with open(f"{id}.json", "w") as f:
        json.dump(data, f, indent=4)
    


