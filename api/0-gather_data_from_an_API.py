#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""
if __name__ == '__main__':
    """TODO list progress."""
    import requests
    import sys

    id = sys.argv[1]
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + id)
    todos = requests.get(
         'https://jsonplaceholder.typicode.com/todos?userId=' + id)

    employee_file = response.json()
    todos_file = todos.json()

    employee_name = employee_file['name']
    total_tasks = len(todos_file)
    completed = sum(1 for todo in todos_file if todo['completed'])
    titles = [todo['title']
             for todo in todos_file if todo['completed']]

    phrase = "is done with tasks"
    print(
        "Employee {} {}({}/{}):".format(employee_name, phrase, completed, total_tasks))
    for title in titles:
        print("\t {}".format(title))

  