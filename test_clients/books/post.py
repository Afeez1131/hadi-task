from decimal import Decimal

import requests
import uuid
from datetime import datetime

BASE_URL = 'http://127.0.0.1:8000/api/books/'


data = {
    'title': 'Django for Dummy',
    'author': 'William S. Vincent',
    'publication_date': datetime.now().date(),
    'isbn': uuid.uuid4().hex[:14].upper(),
    'genre': 'Programming',
    'price': Decimal(134.50)
}

"""Creating new book"""

resp = requests.post(BASE_URL, data=data)
print(resp.json())
