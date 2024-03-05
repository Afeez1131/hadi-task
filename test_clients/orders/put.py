import requests
import random
from datetime import datetime

BASE_URL = 'http://127.0.0.1:8000/api/orders/'
users_url = 'http://127.0.0.1:8000/api/users/'
book_url = 'http://127.0.0.1:8000/api/books/'

users = requests.get(users_url).json()
books = requests.get(book_url).json()
orders = requests.get(BASE_URL).json()

if len(users) > 0 and len(books) > 0 and len(orders) > 0:
    user_id = users[0].get('id')
    book_id = books[0].get('id')
    first = orders[0]
    put_url = BASE_URL + f"{first.get('id')}/"
    print('before full update: ', requests.get(put_url).json())

    data = {
        'book': book_id,
        'user': user_id,
        'quantity': random.randint(25, 50),
        'order_date': datetime.now().date()
    }
    response = requests.put(put_url, data=data)
    print('after update: ', response.json())
else:
    print('not enough record to update.')
