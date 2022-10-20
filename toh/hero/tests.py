from django.test import TestCase, Client
from .models import Hero

# Create your tests here.

class HeroTestCase(TestCase):
    def setUp(self):
        Hero.objects.create(name='super')

    def test_index(self):
        client = Client()
        response = client.get('/hero/')
        self.assertIn(response.data, "1")
        response = client.get('/hero/')
        self.assertIn(response.data, "2")
