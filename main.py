from enum import Enum
from random import randint
class Map:
    def __init__(self, height, width):
        self.grid = self.__generate_initial_map(height,width)
        self.__width = width
        self.__height = height

    def place_object(self, object):
        pass
        
    def __generate_initial_map(self, height:int, width:int):
        map = []
        for i in range(height):
            map.append(['-'] * width)
        map[0][0] = "O"
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

    def generate_stats(self):
        pass

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
        return f"{self.text_color}{self.rarity.value}\033[0m {self.type.value} item!"
    
class Player_Class(Enum):
    WARRIOR = "Warrior"
    MAGE = "Mage"
    ARCHER = "Archer"
    TANK = "Tank"
class Player:
    def __init__(self, name: str, player_class: Player_Class):
        self.name = name
        self.player_class = player_class
        self.position = [0][0]
        
        self.level = 1
        self.exp = 0

        self.health = 5 # change this
        self.armour = 5 # change this
        self.attack = 5 # change this
        self.mana = 5 # change this

        self.inventory = self.starting_items()
        self.equipped = [] # change this

    def move(self, action:str):
        pass

    def is_alive(self):
        return self.health > 0

    def die(self):
        # Reset player back to start of current dungeon, reset map + respawn enemies
        pass

    def take_dmg(self, dmg:int):
        self.health -= dmg
        if self.is_alive() == False:
            self.die()

    def starting_items(self):
        pass

    def display_inventory(self):
        print("------------------ ** INVENTORY ** ------------------")
        for item in self.inventory:
            print(item)

    def display_equipped(self):
        pass

    def display_player_info(self):
        print(f"Character: {self.name} | Class: {self.player_class.value} | Lvl: {self.level}")

    def equip_item(self, item):
        pass

class Enemy_Type(Enum):
    BOSS = "BOSS"
    ELITE = "ELITE"
    COMMON = "ENEMY"
class Enemy:
    def __init__(self, name, health, dmg, armour, enemy_type):
        self.name = name
        self.health = health
        self.dmg = dmg
        self.armour = armour
        self.enemy_type = enemy_type

    def attack(self, player:Player):
        player.take_dmg(self.dmg)

    def take_dmg(self, dmg:int):
        self.health -= dmg
        if self.is_alive() != True: # DEAD
            self.die()

    def is_alive(self):
        return self.health > 0
    
    def die(self): # Need to give exp, drop loot and remove enemy from map
        pass 

    def __str__(self):
        return (f"{self.enemy_type.value} {self.name} (Health:{self.health} Attack:{self.dmg} Armour:{self.armour})")

class Game:
    def __init__(self, player):
        self.is_running = True
        self.player = player

    def menu(self):
        return f"-------------------------- ** MENU ** --------------------------\nWhat action would you like to take: Move[1] Shop[2] Inventory[3] Save & Quit[4] "

    def player_input(self):
        choice = input(self.menu())
        print()
        match choice:
            case "1":
                self.move_input()
            case "2":
                pass
            case "3":
                player.display_inventory()
                player.display_equipped()
            case "4":
                # Add a save function here
                print("** Thanks for playing! **")
                self.is_running = False
        print()

    def move_input(self):
        movement_input = ""
        movement_commands = ["1", "2", "3", "4", "5"]
        while movement_input not in movement_commands:
            movement_input = input("What way would you like to move? UP[1] DOWN[2] LEFT[3] RIGHT[4] CANCEL[5] ")
            if movement_input in movement_commands:
                player.move(movement_input)
            else:
                print("Please enter a valid movement command!")
        print()

map = Map(5,18)
map.display_map()

player = Player("Billy Bob", Player_Class.WARRIOR)
player.inventory = [Item(), Item(), Item(), Item(), Item()]
player.display_inventory()
player.display_player_info()

game = Game(player)
while game.is_running:
    game.player_input()



