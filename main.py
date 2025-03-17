from enum import Enum
from random import randint
class Map:
    def __init__(self, height, width, player_symbol='O'):
        self.__player_symbol = player_symbol
        self.grid = self.__generate_initial_map(height,width)
        self.__width = width
        self.__height = height

    def place_object(self, object):
        pass
        
    def __generate_initial_map(self, height:int, width:int):
        map = []
        for i in range(height):
            map.append(['-'] * width)
        map[0][0] = self.__player_symbol
        return map

    def display_map(self):
        print()
        print("-" * (2 + (self.__width * 5) - 2))
        for row in self.grid:
            print(row)
        print("-" * (2 + (self.__width * 5) - 2))
        print()

class ItemType(Enum):
    WEAPON = "Weapon"
    ARMOR = "Armor"
    POTION = "Potion"
    MISC = "Miscellaneous"
# ANSI escape codes
class Color:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
class Rarity(Enum):
    LEGENDARY = "Legendary"
    ENHANCED = "Enhanced"
    COMMON = "Common"
    BROKEN = "Broken"
class Item:
    def __init__(self):
        self.type = self.generate_type()
        self.text_color = None
        self.rarity = self.generate_rarity()

    def generate_type(self):
        potential_type = list(ItemType)
        random_val = randint(0,len(potential_type)-1)
        return potential_type[random_val]
    
    def generate_rarity(self):
        random_val = randint(0,101)
        if random_val > 98:
            self.text_color = Color.RED
            return Rarity.LEGENDARY
        if random_val > 78:
            self.text_color = Color.PURPLE
            return Rarity.ENHANCED
        if random_val > 28:
            self.text_color = Color.BLUE
            return Rarity.COMMON
        self.text_color = Color.GREEN
        return Rarity.BROKEN

    def __repr__(self):
        return f"{self.text_color}{self.rarity.value} {self.type.value} item!\033[0m"
    
map = Map(5,18)
map.display_map()

items = []
for i in range(100):
    items.append(Item())

for item in items:
    print(item)
