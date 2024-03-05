from decimal import Decimal

import requests
import uuid
from datetime import datetime


BASE_URL = 'http://127.0.0.1:8000/api/books/'
all_books = requests.get(BASE_URL).json()
if len(all_books) > 0:
    first = all_books[0]
    put_url = BASE_URL + f"{str(first.get('id'))}/"
    print('before full update: ', requests.get(put_url).json())

    data = {
        'title': 'Django for Beginners (Updated)',
        'author': 'William S. Vincent',
        'publication_date': datetime.now().date(),
        'isbn': uuid.uuid4().hex[:14].upper(),
        'genre': 'Programming',
        'price': Decimal(150.50)
    }
    response = requests.put(put_url, data=data)
    print('after update: ', response.json())
