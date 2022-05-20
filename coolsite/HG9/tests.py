from django.urls import reverse
from rest_framework.test import APITestCase

class HG9ApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('home')
        print(url)
        response = self.client.get(url)
        print(response)

class HG9ApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('about')
        print(url)
        response = self.client.get(url)
        print(response)

class HG9ApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('add_page')
        print(url)
        response = self.client.get(url)
        print(response)

class HG9ApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('contact')
        print(url)
        response = self.client.get(url)
        print(response)

class HG9ApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('login')
        print(url)
        response = self.client.get(url)
        print(response)