#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import sys
import requests

api_url = "https://jsonplaceholder.typicode.com/"
employee_ID = sys.argv[1]
user = requests.get(api_url + "users/{}".format(employee_ID))
user_data = user.json()
employee_name = user_data['name']
todos = requests.get(api_url + "todos", params={"userId": employee_ID})
todos_data = todos.json()
total_tasks = len(todos_data)
tasks_completed = sum(1 for task in todos_data if task['completed'])
print("Employee {} is done with tasks ({}/{})".format(employee_name, tasks_completed, total_tasks))
for task in todos_data:
    if task['completed']:
        print("\t{}   {}".format(task['title'], task['completed']))
