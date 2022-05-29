import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Careless Whisper")
        self.song2 = Song("Friday")

    def test_has_song1_name(self):
        self.assertEqual("Careless Whisper", self.song1.song_name)

    def test_has_song2_name(self):
        self.assertEqual("Friday", self.song2.song_name)
    
