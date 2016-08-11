from django.test import TestCase
from .models import Staff


class StaffModelCase(TestCase):
    def setUp(self):
        # Setup the data data here
        Staff.objects.create(first_name="Patrick", last_name="Biggs", biography="I am an IT guy")
        Staff.objects.create(first_name="Ramzan", last_name="Jabber", biography="He is an IT guy")

    # Predefine some tests that can't yet be done in order to help development
    # Create a function for each test you want to perform
    def test_Staff_Create_Read(self):
        s1 = Staff.objects.get(first_name="Ramzan")
        s2 = Staff.objects.get(first_name="Patrick")
        self.assertEqual(s1.test(), s1)
        self.assertEqual(s2.test(), s2)

    # Some example tests, i.e. cases that should not occur

    # Don't create a user with the same name as another user



