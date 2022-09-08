#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

url = 'https://jsonplaceholder.typicode.com/'


def print_with_format(employee, todos, employee_todos, completed):
    """Function to print with required format"""
    print('Employee', employee.get('name'),
          'is done with tasks({}/{}):'.
          format(len(completed), len(employee_todos)))
    [print('\t', todo.get('title')) for todo in completed]


def get_data_from_api():
    """
    Function to get data from https://jsonplaceholder.typicode.com/
    """

    """Control input argument"""
    if len(sys.argv) < 2:
        return print('USAGE:', __file__, '<employee id>')
    e_id = sys.argv[1]
    try:
        _e_id = int(sys.argv[1])
    except ValueError:
        return print('Employee id must be an integer')

    """Control respose status for Employee"""
    response = requests.get(url + 'users/' + e_id)
    if response.status_code == 404:
        return print('Employee id not found')
    elif response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    employee = response.json()

    """Control respose status for todos"""
    response = requests.get(url + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()

    """Create a list matching todos for that given Employee ID"""
    employee_todos = [todo for todo in todos
                      if todo.get('userId') == employee.get('id')]

    """Create a list matching completed tasks for that given Employee ID"""
    completed = [todo for todo in employee_todos if todo.get('completed')]

    """print with required format"""
    print_with_format(employee, todos, employee_todos, completed)


if __name__ == "__main__":
    get_data_from_api()
