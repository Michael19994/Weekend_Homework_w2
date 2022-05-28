import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Pop Room")
        self.song1 = Song("Careless Whisper")
        self.song2 = Song("Friday")
        self.guest = Guest("Alex")
        
    def test_has_room_name(self):
        self.assertEqual("Pop Room", self.room1.name)
    
    def test_nobody_starts_in_room(self):
        self.assertEqual(0, self.room1.guest_count())

    def test_add_guest_to_room(self):
        guest = Guest("Alex")
        self.room1.add_guest(guest)
        self.assertEqual(1, self.room1.guest_count())

    def test_remove_guest_from_room(self):
        guest = Guest("Alex")
        self.room1.add_guest(guest)
        self.room1.remove_guest(guest)
        self.assertEqual(0, self.room1.guest_count())

    def test_no_songs_in_room(self):
        self.assertEqual(0, self.room1.song_count())

    def test_add_songs_to_room(self):
        songs = Song("Careless Whisper")
        songs = Song("Friday")
        self.room1.add_songs(songs)
        self.assertEqual






    
        
