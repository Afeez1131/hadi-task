import requests

BASE_URL = 'http://127.0.0.1:8000/api/users/'


data = {
    'username': 'django_user',
    'email': 'django@mail.com',
    'password': 'password'
}

"""Creating new user"""

resp = requests.post(BASE_URL, data=data)
print(resp.json())
