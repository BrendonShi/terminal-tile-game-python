import copy


class Item:
    def __init__(self, id: int, icon: str, name: str, count: int, description: str):
        self.id = id
        self.icon = icon
        self.name = name
        self.count = count
        self.description = description 

    def use(self, player):
        print("Can't be used")

    def __str__(self):
        return f"{self.name}: {self.count} ({self.description})"

class Potion(Item):
    def __init__(self, id: int, icon: str, name: str, count: int, description: str):
        super().__init__(id, icon, name, count, description)


class HealthPotion(Potion):
    def __init__(self, count: int = 1):
        super().__init__(1, "\033[38;5;197m\033[0m", "Healing Potion", count, "This potion heals some of HC")

    def use(self, player):
        if player.hc < player.max_hc:
            player.hc += 2
            player.inventory.remove_item(self)
            if player.hc >= player.max_hc:
                player.hc = player.max_hc
        else:
            print("your hc is full")


class ManaPotion(Potion):
    def __init__(self, count: int = 1):
        super().__init__(2, "\033[38;5;33m\033[0m", "Mana Potion", count, "This potion restores some of mana")

    def use(self, player):
        if player.mana < player.max_mana:
            player.mana += 4
            player.inventory.remove_item(self)
            if player.mana >= player.max_mana:
                player.mana = player.max_mana
        else:
            print("your mana is full")

class Stick(Item):
    def __init__(self, count: int = 1):
        super().__init__(3, "S", "Stick", count, "Just a stick")


class Wood(Item):
    def __init__(self, count: int = 1):
        super().__init__(4, "W", "Wood", count, "Just a wood")


class WoodenSword(Item):
    def __init__(self, count: int = 1):
        super().__init__(5, "S", "Wooden Sword", count, "Sword")


class BlueMango(Item):
    def __init__(self, count: int = 1):
        super().__init__(6, "B", "Blue Mango", count, "Strange Blue Mango")


class MoonFlower(Item):
    def __init__(self, count: int = 1):
        super().__init__(7, "F", "Moon Flower", count, "Looks like flower")


class RedMoonFlower(Item):
    def __init__(self, count: int = 1):
        super().__init__(8, "F", "Red Moon Flower", count, "Looks like flower")


class MonsterEye(Item):
    def __init__(self, count: int = 1):
        super().__init__(9, "E", "Monster Eye", count, "Looks like eye")


class UsefulItems():
    classes = {
        "Stick": Stick(),
        "Wood": Wood(),
        "Wooden Sword": WoodenSword(),
        "Mana Potion": ManaPotion(),
        "Health Potion": HealthPotion(),
        "Blue Mango": BlueMango(),
        "Moon Flower": MoonFlower(),
        "Red Moon Flower": RedMoonFlower(),
        "Monster Eye": MonsterEye()
    }
    @staticmethod
    def get_item_by_name(name):
        return UsefulItems.classes.get(name)

    @staticmethod
    def create_item_instance(name):
        item_template = UsefulItems.get_item_by_name(name)
        new_item = None
        if item_template:
            new_item = copy.deepcopy(item_template)
        return new_item
