class Guest:
    def __init__(self, name, money):
       self.name = name
       self.money = money

    def get_name(self, name):
        return name

    def guest_has_money(self, money):
        return money    
    
    def reduce_money(self,take_away):
        if self.money >= take_away:
            self.money -= take_away

    