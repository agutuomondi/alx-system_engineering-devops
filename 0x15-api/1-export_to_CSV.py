#!/usr/bin/python3
"""
Script that uses JSONPlaceholder API to get information about an employee
and exports TODO list to CSV.

Requirements:
- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv
"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    task = url_user + '/todos'

    res_user = requests.get(url_user)
    user_name = res_user.json().get('username')

    res_tasks = requests.get(task)
    tasks = res_tasks.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
