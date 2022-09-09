#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
export data in the JSON format.
Requirements:
    Records all tasks from all employees
    Format must be: { "USER_ID": [{"username": "USERNAME", "task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
    {"username": "USERNAME", "task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME",
    "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username":
    "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
    ... ]}
    File name must be: todo_all_employees.json
"""
import json
import requests
import sys

url = 'https://jsonplaceholder.typicode.com/'


def save_to_json(data):
    """Function to save to JSON file"""
    with open('todo_all_employees.json', 'w') as jsonf:
        json.dump(data, jsonf)


def get_data_from_api():
    """
    Function to get data from https://jsonplaceholder.typicode.com/
    """
    """Control respose status for all Employees"""
    response = requests.get(url + 'users/')
    if response.status_code == 404:
        return print('Employees not found')
    elif response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    employees = response.json()

    """Control respose status for todos"""
    response = requests.get(url + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()

    """Create a dictionary matching todos for all Employees"""
    data = {}
    for employee in employees:
        employee_todos = [todo for todo in todos
                          if todo.get('userId') == employee.get('id')]
        employee_todos = [{'username': employee.get('username'),
                           'task': todo.get('title'),
                           'completed': todo.get('completed')}
                          for todo in employee_todos]
        data[str(employee.get('id'))] = employee_todos

    """Save to JSON file with required format"""
    save_to_json(data)


if __name__ == "__main__":
    get_data_from_api()
