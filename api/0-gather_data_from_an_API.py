#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import requests
import sys
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""
if __name__ == '__main__':
    """ TODO list progress."""
    id = sys.argv[1]
    title = []
    complete = 0
    tasks = 0
    url_user = "https://jsonplaceholder.typicode.com/users/" + id
    res = requests.get(url_user).json()
    name = res.get('name')
    tasks = "https://jsonplaceholder.typicode.com/todos/"
    res_tasks = requests.get(tasks).json()
    for i in res_tasks:
        if i.get('userId') == int(id):
            if i.get('completed') is True:
                title.append(i['title'])
                complete += 1
            tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, complete, tasks))
    for x in title:
        print("\t {}".format(x))