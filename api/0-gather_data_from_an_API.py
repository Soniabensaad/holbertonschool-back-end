#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""
import requests
import sys
if __name__ == '__main__':
    """ for a given employee ID, returns information about
        his/her TODO list progress."""
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")


    if response.status_code != 200:
        sys.exit(1)
  

    tasks = response.json()

    total_tasks = len(tasks)
    done_tasks = sum(task["completed"] for task in tasks)
    employee_name = tasks[0]["username"]

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in tasks:
       if task["completed"]:
           print(f"\t {task['title']}")
