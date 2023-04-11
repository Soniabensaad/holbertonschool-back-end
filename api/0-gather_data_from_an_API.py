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
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(
        api_url + "todos", params={"userId": sys.argv[1]}).json()

    complete = []
    for task in todos:
        if task.get("completed") is True:
            complete.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(complete), len(todos)))
    for i in complete:
        print("\t {}".format(i))