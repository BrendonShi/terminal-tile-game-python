from container import Inventory
from vector import Vector2D
from accessories import AccessoriesHolder
from alert import notification_alert


class Player:
    def __init__(self, name, hc, mana, min_damage, max_damage):
        self.name = name
        self.max_hc = 4
        self.hc = hc
        self.max_mana = 20
        self.mana = mana
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.inventory = Inventory()
        self.position = Vector2D(0, 0)
        self.accessories = AccessoriesHolder()


    def add_hc(self, amount):
        if self.hc < self.max_hc:
            self.hc += amount
            if self.hc > self.max_hc:
                self.hc = self.max_hc
        else:
            notification_alert.alert("Your HC is full")


    def show_stats(self):
        print(f"{self.name} (alive?)")
        empty_hearts = self.max_hc - self.hc
        print("HC:", self.hc*"\033[38;5;197m♡\033[0m"+empty_hearts*"\033[38;5;239m♡\033[0m")
        empty_mana_points = self.max_mana - self.mana
        print("MaNa:", self.mana*"\033[38;5;51m\033[0m"+empty_mana_points*"\033[38;5;239m\033[0m")
        print("Damage:", self.min_damage, "-", self.max_damage)
        #print(f"Mana: {self.mana}")
        #print(f"Min Damage: {self.min_damage}")
        #print(f"Max Damage: {self.max_damage}")
