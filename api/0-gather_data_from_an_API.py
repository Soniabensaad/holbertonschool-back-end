#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    """TODO list progress."""

    url = "https://jsonplaceholder.typicode.com/"

    
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(sys.argv[1])).json()

   
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()

    

    finished_tasks = [task.get("title") for task in todos if
                      task.get("completed") is True]

    
    print("Employee {} is done with tasks({}/{}):".format(
        users.get("name"), len(finished_tasks), len(todos)))

    [print("\t {}".format(finished)) for finished in finished_tasks]
