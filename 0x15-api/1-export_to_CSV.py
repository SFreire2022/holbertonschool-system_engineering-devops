#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
export data in the CSV format.
Requirements:
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""
import csv
import requests
import sys

url = 'https://jsonplaceholder.typicode.com/'


def save_to_csv(e_id, employee, employee_todos):
    """Function to save to CSV file"""
    with open(e_id + '.csv', 'w') as csvf:
        writer = csv.writer(csvf, lineterminator='\n',
                            quoting=csv.QUOTE_ALL)
        [writer.writerow(['{}'.format(field) for field in
                          (todo.get('userId'), employee.get('username'),
                           todo.get('completed'), todo.get('title'))])
         for todo in employee_todos]


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

    """Control respose status for Employee id"""
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

    """Save to CSV file with required format"""
    save_to_csv(e_id, employee, employee_todos)


if __name__ == "__main__":
    get_data_from_api()
