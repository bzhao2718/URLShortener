from django.test import TestCase
from URLShortener.models import ShortURL
from django.contrib.auth.models import User
from django.test import TestCase, Client
import datetime, os


class TestShortURLModel(TestCase):
    def test_create_shorturl(self):
        original_url = "https://www.django-rest-framework.org"
        url_key = "restapi"
        date = datetime.datetime.now()
        shorturl=ShortURL.objects.create(original_url=original_url,url_key=url_key,created_time=date)

        self.assertIsInstance(shorturl, ShortURL)
        self.assertEquals(original_url, shorturl.original_url)
        self.assertEquals(url_key, shorturl.url_key)
        self.assertEquals(date, shorturl.created_time)
        self.assertIsNone(shorturl.user_id)


class TestUser(TestCase):
    """Test the core methods relating to user creation and login"""

    def setUp(self):
        new_user = User.objects.create_user(username="testUser", password="@user1234test")
        new_user.save()
        self.client = Client()

    def test_user_auth(self):
        login = self.client.login(username="testUser", password="@user1234test")
        # response = self.client.get("/test/greet_user")
        created_user = User.objects.get(username="testUser")
        self.assertIsNotNone(created_user)


class TestURLShortener(TestCase):
    """Test the core methods of URLShortener"""

    def setUp(self):
        login = self.client.login(username="testUser",password="@user1234test")
        if not login:
            new_user = User.objects.create_user(username="testUser",password="@user1234test")
            new_user.save()
        self.client = Client()

    def test_user_login(self):
        login = self.client.login(username="testUser",password="@user1234test")
        self.assertTrue(login)