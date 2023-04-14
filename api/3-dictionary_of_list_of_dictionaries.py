#!/usr/bin/python3
"""Using what you did in the task #0
 extend your Python script
 to export data in the JSON format."""

import json
import requests
import sys
if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(url + "users/").json()
    todo_data = requests.get(url + "todos?userId=").json()

    user_dict = {}
    for user in user_data:
        user_id = user["id"]
        username = user["username"]
    user_dict[user_id ] = []
    for todo in todo_data:
        if user_id == todo["users_id"]:
            user_dict[user_id].append({
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]

            })

        

    with open("todo_all_employees.json", "w") as f:
        json.dump(user_id, f)
