import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Alex")
        self.guest2 = Guest("Ramon")
        self.guest3 = Guest("David")

    def test_has_name(self):
        self.assertEqual("Alex", self.guest.name)

   