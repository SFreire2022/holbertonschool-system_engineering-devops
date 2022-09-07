#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def get_data_from_api():
    """
    Function to get data from https://jsonplaceholder.typicode.com/
    """
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    completed = [t.get('title') for t in todos if t.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get('name'), len(completed), len(todos)))
    [print('\t {}'.format(c)) for c in completed]


if __name__ == "__main__":
    get_data_from_api()
