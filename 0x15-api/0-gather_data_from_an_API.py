#!/usr/bin/python3

"""
Script to retrieve and display TODO list progress for a given employee
using a REST API.

Requirements:
- Use urllib or requests module
- Accept an integer as a parameter (employee ID)
- Display progress information in the specified format
"""

import re
import requests
import sys


if __name__ == '__main__':
    REST_API = "https://jsonplaceholder.typicode.com"  # Moved up here
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
