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


data = {
    'title': 'Django for Dummy',
    'author': 'William S. Vincent',
    'publication_date': datetime.now().date(),
    'isbn': uuid.uuid4().hex[:14].upper(),
    'genre': 'Programming',
    'price': Decimal(134.50)
}

"""Creating new book"""
if header:
    resp = requests.post(BASE_URL, data=data, headers=header)
    print(resp.json())
else:
    print(f'invalid authentication header {header}')
