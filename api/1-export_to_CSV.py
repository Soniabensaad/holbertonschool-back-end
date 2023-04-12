#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the CSV format.
Records all tasks that are owned by this employee
Format must be:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/" + user_id
    res = requests.get(url_user).json()
    username = res.get("username")
    req = requests.get(
        "https://jsonplaceholder.typicode.com/users/" +
        (user_id) + '/todos')
    with open("{}.csv".format(sys.argv[1]), "w") as file_c:
        writer = csv.writer(file_c, quoting=csv.QUOTE_ALL)
        for task in req.json():
            writer.writerow([user_id, username,
                            task.get("completed"), task.get("title")])
