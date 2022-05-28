from classes.guest import Guest
from classes.song import Song


class Room:
    def __init__(self, name):
        self.name = name
        self.guest_number = 0
        self.guest_list = []
        self.amount_of_songs = 0
        self.song_list = []
    

    def guest_count(self):
        return self.guest_number
    
    def add_guest(self, guest):
        self.guest_number += 1
        self.guest_list.append(guest)
    
    def remove_guest(self, guest):
        self.guest_number -= 1
        self.guest_list.remove(guest)

    def song_count(self):
        return self.amount_of_songs

    def add_songs(self,songs):
        self.amount_of_songs += 2
        self.song_list.append(songs)


