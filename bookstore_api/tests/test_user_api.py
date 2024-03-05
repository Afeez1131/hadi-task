import uuid
from datetime import datetime
from decimal import Decimal

import requests
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from .test_models import create_book, create_user

from django.contrib.auth.models import User

USER_URL = 'http://localhost:8000/api/users/'
USER_INSTANCE_URL = USER_URL + '1/'
AUTH_URL = 'http://127.0.0.1:8000/api/token-auth'


def get_user_data():
    return {
        'username': 'test_user',
        'email': 'test@mail.com',
        'password': 'password',
    }


def get_auth_headers(token):
    return {'Authorization': 'Token ' + token}


class UserApiTest(TestCase):
    """Test case for the User API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user()
        auth_data = {
            'username': 'admin',
            'password': 'password',
            'email': 'admin@gmail.com'
        }
        self.user = create_user(**auth_data)
        token, _ = Token.objects.get_or_create(user=self.user)
        self.headers = get_auth_headers(token.key)

    def test_user_not_created_without_valid_headers(self):
        response = self.client.post(USER_URL, data=get_user_data())
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_creation(self):
        response = self.client.post(USER_URL, data=get_user_data(), headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_users(self):
        response = self.client.get(USER_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get('results')), 2)


class UserInstanceApiTest(TestCase):
    """Test case for the User Instance API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user()
        auth_data = {
            'username': 'admin',
            'password': 'password',
            'email': 'admin@gmail.com'
        }
        self.user = create_user(**auth_data)
        token, _ = Token.objects.get_or_create(user=self.user)
        self.headers = get_auth_headers(token.key)

    def test_get_user_instance(self):
        response = self.client.get(USER_INSTANCE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_instance(self):
        data = {
            'username': 'update',
            'email': 'update@gmail.com',
            'password': 'password'
        }
        response = self.client.put(USER_INSTANCE_URL, data=data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_not_supported(self):
        data = {
            'username': 'new_username'
        }
        response = self.client.patch(USER_INSTANCE_URL, data=data, headers=self.headers)
        self.assertNotEqual(response.json(), status.HTTP_200_OK)
