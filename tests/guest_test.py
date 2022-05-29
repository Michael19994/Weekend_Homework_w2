import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Alex", 20)

    def test_has_name(self):
        self.assertEqual("Alex", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(20, self.guest.money)

    def test_decrease_money(self):
        self.guest.reduce_money(10)
        self.assertEqual(10, self.guest.money)



        