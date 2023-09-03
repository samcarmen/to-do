from unittest import mock
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class GoogleLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    @mock.patch("requests.post")
    @mock.patch("requests.get")
    def test_google_callback(self, mock_get, mock_post):
        # Mock the POST request to get the access token
        mock_post.return_value.json.return_value = {
            "access_token": "mock_access_token",
        }

        # Mock the GET request to get user info
        mock_get.return_value.json.return_value = {
            "email": "mockemail@gmail.com",
            "given_name": "Mock",
            "family_name": "Name",
        }

        # Mimic the callback with the 'code'
        response = self.client.get(
            "/todo/callback/",
            {"code": "mock_auth_code"},
        )

        # Check if user is created and redirected to home
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertEqual(response.url, "/todo/home/")  # Redirect URL

        # Check if user is created
        user = User.objects.get(email="mockemail@gmail.com")
        self.assertIsNotNone(user)

        # Check if DRF token is created
        drf_token = Token.objects.get(user=user)
        self.assertIsNotNone(drf_token)
