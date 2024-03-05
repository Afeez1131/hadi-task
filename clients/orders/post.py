import requests
import random

AUTH_URL = 'http://127.0.0.1:8000/api/token-auth'
auth_data = {'username': 'admin', 'password': 'password',}

response = requests.post(AUTH_URL, data=auth_data)
json_response = response.json()
if response.status_code != 200:
    header = {}
else:
    token = json_response.get('token')
    header = {'Authorization': 'Token ' + token}

users_url = 'http://127.0.0.1:8000/api/users/'
book_url = 'http://127.0.0.1:8000/api/books/'
BASE_URL = 'http://127.0.0.1:8000/api/orders/'
if header:
    users = requests.get(users_url, headers=header).json()
    books = requests.get(book_url, headers=header).json()
    # print(users, books)
    if len(users) > 0 and len(books) > 0:
        user_id = users[0].get('id')
        book_id = books[0].get('id')
        data = {
            'user': user_id,
            'book': book_id,
            'quantity': random.randint(1, 20)
        }
        resp = requests.post(BASE_URL, data=data, headers=header)
        print(resp.json())
    else:
        print('Not enough Users and book records.')
else:
    print(f'invalid authentication header {header}')
