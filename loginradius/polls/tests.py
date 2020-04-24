from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Contestant

class AnimalTestCase(TestCase):
    def setUp(self):
        Contestant.objects.create(contestant_name="lion", votes=1000)
        Contestant.objects.create(contestant_name="cat", votes=10)