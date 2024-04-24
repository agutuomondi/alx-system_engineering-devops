#!/usr/bin/python3
'''
Script to retrieve and display TODO list progress for a given employee
using a REST API.

Requirements:
- Use urllib or requests module
- Accept an integer as a parameter (employee ID)
- Display progress information in the specified format
'''

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

def fetch_employee_data(employee_id):
    req = requests.get(f"{REST_API}/users/{employee_id}").json()
    task_req = requests.get(f"{REST_API}/todos").json()
    emp_name = req.get('name')
    tasks = [task for task in task_req if task.get('userId') == employee_id]
    completed_tasks = [task for task in tasks if task.get('completed')]
    return emp_name, len(completed_tasks), len(tasks), completed_tasks

if __name__ == '__main__':
    if len(sys.argv) > 1 and re.fullmatch(r'\d+', sys.argv[1]):
        employee_id = int(sys.argv[1])
        emp_name, completed_count, total_count, completed_tasks = fetch_employee_data(employee_id)
        print(f"Employee {emp_name} is done with tasks({completed_count}/{total_count}):")
        if completed_count > 0:
            for task in completed_tasks:
                print(f"\t {task.get('title')}")
