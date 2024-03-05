from decimal import Decimal

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
        print('all_books: ', all_books, '\n')
        first = all_books.get('results')[0]
        put_url = BASE_URL + f"{str(first.get('id'))}/"
        print('before full update: ', requests.get(put_url, headers=header).json())

        data = {
            'title': 'Django for Beginners (Updated)',
            'author': 'William S. Vincent',
            'publication_date': datetime.now().date(),
            'isbn': uuid.uuid4().hex[:14].upper(),
            'genre': 'Programming',
            'price': Decimal(150.50)
        }
        response = requests.put(put_url, data=data, headers=header)
        print('after update: ', response.json())
else:
    print(f'invalid authentication header {header}')
