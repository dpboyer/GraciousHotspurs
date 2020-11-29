from django.test import TestCase
from .models import MyUser

# Create your tests here.


class AddUserTest(TestCase):
    # checks for a User being created correctly
    def test_user_matchName(self):
        username = "test"
        testUser = MyUser(name = username)
        self.assertEqual(username, str(testUser))

    # checks for a User being created correctly
    def test_user_matchPassword(self):
        password = "1234"
        testUser = MyUser(password = password)
        self.assertEqual(password, str(testUser))

    # checks for a User being created correctly
    def test_user_matchBoth(self):
        username = "test"
        password = "1234"
        testUser = MyUser(name = username, password = password)
        self.assertEqual(username+password, str(testUser))

    # checks that a User can be saved to the database
    def test_user_saveToDatabase(self):
        testUser = MyUser(name = "test", password = "1234")
        testUser.save()