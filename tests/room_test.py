import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Pop Room")
        self.song1 = Song("Careless Whisper")
        self.guest = Guest("Alex", 20)
        
    def test_has_room_name(self):
        self.assertEqual("Pop Room", self.room1.name)
    
    def test_if_room_has_entry_fee(self):
        self.assertEqual(10, self.room1.entry_cost)

    def test_room_has_own_tab(self):
        self.assertEqual(200, self.room1.tab)

    def test_if_room_has_space(self):
        self.assertEqual(True, self.room1.room_has_space())

    def test_room_has_no_space(self):
        self.room_full = Room("Pop Room")
        self.room_full.max_amount_guests = 0
        self.assertEqual(True, self.room1.room_has_space())
    
    def test_guest_has_money_to_get_in(self):
        pass
    



    
        
