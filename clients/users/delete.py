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
if header:
    all_users = requests.get(BASE_URL, headers=header).json()
    if len(all_users) > 0:
        last = all_users[-1]
        delete_url = BASE_URL + f"{last.get('id')}/"
        print('deleting user:', delete_url)
        count = len(requests.get(BASE_URL, headers=header).json())
        print(f'before delete, we have {count} users')
        response = requests.delete(delete_url, headers=header)
        count = len(requests.get(BASE_URL, headers=header).json())
        print(f'after delete, we have {count} users left')
else:
    print(f'invalid header: {header}')
