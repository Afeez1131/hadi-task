import requests

BASE_URL = 'http://127.0.0.1:8000/api/users/'
all_users = requests.get(BASE_URL).json()
if len(all_users) > 0:
    first = all_users[0]
    put_url = BASE_URL + f"{first.get('id')}/"
    print('before full update: ', requests.get(put_url).json())

    data = {
        'username': 'django-user',
        'email': 'django-user@gmail.com',
        'password': 'testpass123',
    }
    response = requests.put(put_url, data=data)
    print('after update: ', response.json())
