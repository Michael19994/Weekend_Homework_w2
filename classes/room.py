from classes.guest import Guest
from classes.song import Song

class Room:
    def __init__(self, name):
        self.name = name
        self.max_amount_guests = 15
        self.entry_cost = 10
        self.tab = 200
        self.guest_list = []
        self.song_list = []

    def room_has_name(self):
        return self.name

    def cost_to_enter_room(self, guest):
        return guest.money > self.entry_cost

    def take_money_from_guest(self, guest):
        if self.cost_to_enter_room:
            guest.money -= self.entry_cost
    
    def guest_money_into_tab(self, money):
        self.tab += money
    
    def room_has_space(self):
        return len(self.guest_list) < self.max_amount_guests

    def add_guests(self, guest):
        self.guest_list.append(guest)
    
    def song_in_song_list(self, find_song):
        for song in self.song_list:
            if song.name == find_song:
                return True
        return False

    


