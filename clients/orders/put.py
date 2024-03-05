import requests
import random
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

BASE_URL = 'http://127.0.0.1:8000/api/orders/'
users_url = 'http://127.0.0.1:8000/api/users/'
book_url = 'http://127.0.0.1:8000/api/books/'

if header:
    users = requests.get(users_url, headers=header).json().get('results')
    books = requests.get(book_url, headers=header).json().get("results")
    orders = requests.get(BASE_URL, headers=header).json().get('results')

    if len(users) > 0 and len(books) > 0 and len(orders) > 0:
        user_id = users[0].get('id')
        book_id = books[0].get('id')
        first = orders[0]
        put_url = BASE_URL + f"{first.get('id')}/"
        print('before full update: ', requests.get(put_url, headers=header).json())

        data = {
            'book': book_id,
            'user': user_id,
            'quantity': 1,
            'created': datetime.now().date()
        }
        response = requests.put(put_url, data=data, headers=header)
        print('after update: ', response.json())
    else:
        print('not enough record to update.')
else:
    print(f'invaid authentication header {header}')
