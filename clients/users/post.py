import requests

AUTH_URL = 'http://127.0.0.1:8000/api/token-auth'
auth_data = {'username': 'admin', 'password': 'password',}

response = requests.post(AUTH_URL, data=auth_data)
json_response = response.json()
if response.status_code != 200:
    header = {}
else:
    token = json_response.get('token')
    header = {'Authorization': 'Token ' + token}

BASE_URL = 'http://127.0.0.1:8000/api/users/'

data = {
    'username': 'django_user-2',
    'email': 'django@mail.com',
    'password': 'password'
}

"""Creating new user"""
if header:
    resp = requests.post(BASE_URL, data=data, headers=header)
    print(resp.json())
else:
    print(f'invalid header {header}')
