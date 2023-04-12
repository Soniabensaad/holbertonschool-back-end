#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
export data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/" + id
    res = requests.get(url_user).json()
    username = res.get("username")
    req = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (id) + '/todos')
    with open("{}.csv".format(sys.argv[1]), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in req.json():
            writer.writerow([id, username,
                            task.get("completed"), task.get("title")])