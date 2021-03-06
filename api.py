import json
import sys
from pprint import pprint

import requests
import json


# Using an API with Query Parameters
# parameters = {"id": 1}
# response = requests.get("https://jsonplaceholder.typicode.com/todos", params=parameters)

# *** GET METHOD ***
def get_method():
    """
    The function makes a GET request to the API endpoint, and then prints the response
    """
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    # create a formatted string of the Python JSON object
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    print(text)
    print(""" GET METHOD """)


# get_method()

# *** POST METHOD ***


def post_method():
    """
    We're sending a POST request to the API endpoint, with a JSON object as the data, and the
    Content-Type header set to application/json
    """
    api_url = "https://jsonplaceholder.typicode.com/todos"
    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    headers = {"Content-Type": "application/json"}
    response = requests.post(api_url, data=json.dumps(todo), headers=headers)
    response_json = {
        "data": response.json(),
        "message": response.status_code
    }
    pprint((response_json))
    print(""" POST METHOD """)


# post_method()

# *** PUT / PATCH  METHOD ***


def put_method():
    """
    We're sending a PUT request to the API endpoint, with the data we want to update, and the headers
    """
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    todo = {"userId": 1, "title": "Buy milk", "completed": True}
    headers = {"Content-Type": "application/json"}
    response = requests.put(api_url, data=json.dumps(todo), headers=headers)
    response_json = {
        "data": response.json(),
        "message": response.status_code
    }
    print(response_json)
    print(""" PUT / PATCH METHOD """)


# put_method()


# *** DELETE METHOD ***

def delete_method():
    """
    It sends a DELETE request to the API endpoint and returns the response
    """
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.delete(api_url)
    response_json = {
        "data": response.json(),
        "message": response.status_code
    }
    print(response_json)
    print(""" DELETE METHOD """)


# delete_method()

response = requests.get("https://jsonplaceholder.typicode.com/todos")
def response_method():
    # It's returning a list of all the attributes and methods of the response object.
    dir(response)
    
    # It's returning the response body as a string.
    response.text 
    
    # It's returning the response body as a byte string.
    response.content 
    
    # It's writing the response content to a file called comic.png.
    with open('comic.png','wb') as f:
        f.write(response.content)

    # It's returning the response headers as a dictionary.
    response.headers
    

def parameters_method():
    """
    The function parameters_method() makes a GET request to the URL https://httpbin.org/get, and passes
    the parameters page=2 and count=25 in the query string.
    """
    payload={'page':2,'count':25}
    response=requests.get("https://httpbin.org/get",params=payload)