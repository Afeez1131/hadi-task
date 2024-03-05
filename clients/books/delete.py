
import requests
import uuid
from datetime import datetime

AUTH_URL = 'http://127.0.0.1:8000/api/token-auth'
auth_data = {'username': 'admin', 'password': 'password',}

response = requests.post(AUTH_URL, data=auth_data)
json_response = response.json()
if response.status_code != 200:
    header = {}
else:
    token = json_response.get('token')
    header = {'Authorization': 'Token ' + token}

BASE_URL = 'http://127.0.0.1:8000/api/books/'
if header:
    all_books = requests.get(BASE_URL, headers=header).json()
    if len(all_books) > 0:
        first = all_books.get('results')[0]
        delete_url = BASE_URL + f"{str(first.get('id'))}/"
        print('deleting book:', delete_url)
        count = len(requests.get(BASE_URL, headers=header).json().get('results'))
        print(f'before delete, we have {count} books')
        response = requests.delete(delete_url, headers=header)
        count = len(requests.get(BASE_URL, headers=header).json().get('results'))
        print(f'after delete, we have {count} books left')
else:
    print(f'invalid authentication header {header}')

