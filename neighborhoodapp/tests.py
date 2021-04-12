from django.test import TestCase
from django.contrib.auth.models import User
from .models import Admin, Amenity, Post, Neighbourhood, Occupant, Business

class AdminTestClass(TestCase):
    def setUp(self):
        self.ryan = User(username = "ryan", email = "ryan@gmail.com",password = "1234")
        self.admin = Admin(user= self.ryan)
        self.ryan.save()
        self.admin.save()

    def tearDown(self):
        Admin.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.ryan, User))
        self.assertTrue(isinstance(self.admin, Admin))

class OccupantTestClass(TestCase):
    def setUp(self):
        self.ryan = User(username = "ryan", email = "ryan@gmail.com",password = "1234")
        self.occupant = Occupant(user= self.ryan, profile_pic='mepng')
        self.ryan.save()
        self.occupant.save()

    def tearDown(self):
        Occupant.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.ryan, User))
        self.assertTrue(isinstance(self.occupant, Occupant))