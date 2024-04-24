#!/usr/bin/python3
"""
Script that uses JSONPlaceholder API to get information about an employee
and exports TODO list to JSON.

Requirements:
- Records all tasks that are owned by this employee
- Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
- File name must be: USER_ID.json
"""
import json
import requests
import sys
import csv


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    url_to_task = url_to_user + '/todos'

    res = requests.get(url_to_user)
    USERNAME = res.json().get('username')

    res = requests.get(url_to_task)
    tasks = res.json()

    dict_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})

    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f)

