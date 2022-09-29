class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
        


class Menu:
    def __init__(self, name, item, start_time, end_time):
        self.name = name
        self.item = item
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self) -> str:
        return self.name + ' menu available from ' + str(self.start_time) + ' - ' + str(self.end_time) 

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill 


brunch = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 
    'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu = Menu('Brunch', brunch, 1100, 1600)
brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee'])

early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu = Menu('Early Bird', early_bird, 1500, 1800)
early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])

dinner = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids = {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
}

menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)