from django.test import TestCase
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.shortcuts import get_object_or_404


class TestProfileViews(TestCase):
    """
    Test the profile page class
    """
    def setUp(self):
        """Set up a test user"""
        username = 'tester'
        email = 'tester@test.com'
        password = 'password'
        user = get_user_model()
        self.user = user.objects.create_user(
            username=username,
            email=email,
            password=password
        )

    def test_profile_page(self):
        """Testing profile page"""
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 404)
