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
all_users = requests.get(BASE_URL, headers=header).json().get('results')
if len(all_users) > 0:
    first = all_users[0]
    put_url = BASE_URL + f"{first.get('id')}/"
    print('before full update: ', requests.get(put_url, headers=header).json())

    data = {
        'username': 'django-user',
        'email': 'django-user@gmail.com',
        'password': 'testpass123',
    }
    response = requests.put(put_url, data=data, headers=header)
    print('after update: ', response.json())
