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
    id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/" + id
    user_data = requests.get(url_user).json()
    username = user_data.get('username')
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (id) + '/todos')
    with open("{}.csv".format(id), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks.json():
            writer.writerow([id, username,
                            task.get("completed"), task.get("title")])
