#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import requests
import sys
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""
if __name__ == "__main__":
    """Write a Python script that, using this REST API,
      for a given employee ID, returns information
      about his/her TODO list progress."""
    api_url = "https://jsonplaceholder.typicode.com/"
    employee_ID = sys.argv[1]
    user = requests.get(api_url + "users/{}".format(employee_ID)).json()
    todos = requests.get(api_url + "todos", params={"userId": employee_ID}).json()
    complete = []
    for task in todos:
        if task.get("completed") is True:
            complete.append(task.get("title"))
    print("Employee {} is done with tasks({}/{})".
          format(task.get("name"), len(complete), len(todos)))
    for i in complete:
        print("\t {}".format(complete))
