from item import Item


class Potion(Item):
    def __init__(self, id: int, icon: str, name: str, count: int, description: str):
        super().__init__(id, icon, name, count, description)


class HealthPotion(Potion):
    def __init__(self, count: int):
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
    def __init__(self, count: int):
        super().__init__(2, "\033[38;5;33m\033[0m", "Mana Potion", count, "This potion restores some of mana")
    
    def use(self, player):
        if player.mana < player.max_mana:
            player.mana += 4
            player.inventory.remove_item(self)
            if player.mana >= player.max_mana:
                player.mana = player.max_mana
        else:
            print("your mana is full")
