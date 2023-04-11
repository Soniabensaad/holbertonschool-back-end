#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""
import requests
import sys

# check if the correct number of arguments is provided
if len(sys.argv) != 2:
    sys.exit(1)

# get the employee ID from the command line argument
employee_id = sys.argv[1]

# make the API request
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

# check if the API request was successful
if response.status_code != 200:
    sys.exit(1)

# parse the API response
tasks = response.json()

# calculate the progress of the employee's TODO list
total_tasks = len(tasks)
done_tasks = sum(task["completed"] for task in tasks)
employee_name = tasks[0]["username"]

# display the progress of the employee's TODO list
print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
for task in tasks:
    if task["completed"]:
        print(f"\t {task['title']}")
