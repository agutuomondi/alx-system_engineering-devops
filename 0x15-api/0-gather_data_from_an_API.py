#!/usr/bin/python3
'''
Script to retrieve and display TODO list progress for a given employee
using a REST API.

Requirements:
- Use urllib or requests module
- Accept an integer as a parameter (employee ID)
- Display progress information in the specified format
'''

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        id = int(sys.argv[1])
        req = requests.get(f"{REST_API}/users/{id}").json()
        task_req = requests.get(f"{REST_API}/todos").json()
        emp_name = req.get('name')
        tasks = [task for task in task_req if task.get('userId') == id]
        completed_tasks = [task for task in tasks if task.get('completed')]
        print(
            f"Employee {emp_name} is done with tasks({len(completed_tasks)}/{len(tasks)}):"
        )
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

