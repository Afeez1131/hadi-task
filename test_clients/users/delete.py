import requests

BASE_URL = 'http://127.0.0.1:8000/api/users/'
all_users = requests.get(BASE_URL).json()
if len(all_users) > 0:
    last = all_users[-1]
    delete_url = BASE_URL + f"{last.get('id')}/"
    print('deleting user:', delete_url)
    count = len(requests.get(BASE_URL).json())
    print(f'before delete, we have {count} users')
    response = requests.delete(delete_url)
    count = len(requests.get(BASE_URL).json())
    print(f'after delete, we have {count} users left')
