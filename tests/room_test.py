import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Pop Room")
        self.song1 = Song("Careless Whisper")
        self.guest = Guest("Alex", 20)
        self.guest2 = Guest("David", 0)
        
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
        self.assertEqual(True, self.room1.cost_to_enter_room(self.guest))
    
    def test_guest_has_no_money_to_get_in(self):
        self.guest_no_money = Guest("David", 0)
        self.assertEqual(False, self.room1.cost_to_enter_room(self.guest_no_money))

    def test_money_transfer_from_guest(self):
        self.room1.take_money_from_guest(self.guest)
        self.assertEqual(10, self.guest.money)
    
    def test_add_tab_to_room(self):
        self.room1.guest_money_into_tab(self.room1.entry_cost)
        self.assertEqual(210, self.room1.tab)

    def test_add_guest_to_guest_list_for_room(self):
        self.room1.add_guests(self.guest)
        self.assertEqual("Alex", self.room1.guest_list[0].name)
    
    def test_song_not_in_song_list_for_room(self):
        self.assertEqual(False, self.room1.song_in_song_list(self.song1))
