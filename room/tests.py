from django.test import TestCase
from .models import Room


class RoomModelCase(TestCase):
    def setUp(self):
        # Setup the data data here
        Room.objects.create(name="Test Room")
        Room.objects.create(name="Test Room")

    # Predefine some tests that can't yet be done in order to help development
    # Create a function for each test you want to perform
    def test_duplicate_rooms(self):
        results = Room.objects.get(name="Test Room")

        self.assertEqual(results.length(), 1)

    # Some example tests, i.e. cases that should not occur

    # Don't create two rooms with the same name

