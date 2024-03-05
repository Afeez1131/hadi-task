import requests
import random

users_url = 'http://127.0.0.1:8000/api/users/'
book_url = 'http://127.0.0.1:8000/api/books/'
BASE_URL = 'http://127.0.0.1:8000/api/orders/'

users = requests.get(users_url).json()
books = requests.get(book_url).json()
# print(users, books)
if len(users) > 0 and len(books) > 0:
    user_id = users[0].get('id')
    book_id = books[0].get('id')
    data = {
        'user': user_id,
        'book': book_id,
        'quantity': random.randint(1, 20)
    }
    resp = requests.post(BASE_URL, data=data)
    print(resp.json())
else:
    print('Not enough Users and book records.')

