#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the CSV format.
Records all tasks that are owned by this employee
Format must be:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

if __name__ == '__main__':
    import csv
    import requests
    import sys

    id = sys.argv[1]
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + id)
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + id)

    data = response.json()
    todos = todos.json()
    id = data['id']
    name = data['username']

    with open(f'{id}.csv', 'w') as file:
        for i in todos:
            Task = i['completed']
            TASK_TITLE = i['title']
            TASK_COMPLETED_STATUS = i['completed']
            TASK_TITLE = i['title']
            file.write(
                f"\"{id}\",\"{name}\",\"{Task}\",\"{TASK_TITLE}\"\n")
