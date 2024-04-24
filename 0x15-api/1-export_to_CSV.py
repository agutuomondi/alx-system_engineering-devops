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
    user_id = sys.argv[1]
    url_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    res = requests.get(url_user)
    user_name = res.json().get('username')
    task_url = f'{url_user}/todos'
    res = requests.get(task_url)
    tasks = res.json()

    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csv_writer.writerow([user_id, user_name, completed, title_task])

