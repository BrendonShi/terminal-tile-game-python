from alert import notification_alert
# from container import CraftingTable
# from vector import Vector2D
from signalclass import Signal


class Object:
    def __init__(self, icon: str, name: str, solid: bool = True):
        self.icon = icon
        self.name = name
        self.solid = solid
        # self.position = Vector2D(0, 0)
        self.interacted = Signal()

    def interact(self):
        # notification_alert.alert(f"You cannot interact with the {self.name}.")
        pass

    def __str__(self):
        return f"{self.icon} {self.name}"

    def __repr__(self):
        return f"{self.icon} {self.name}"


class Wall(Object):
    def __init__(self):
        super().__init__("#", "Wall", solid=True)


class DoorObject(Object):
    def __init__(self, room_id: str):
        super().__init__("D", "Door", solid=True)
        self.room_id = room_id
    
    def interact(self):
        notification_alert.alert(f"You opened the door to room {self.room_id}!")
        # self.solid = False # Allows the player to move through it after "opening" it.


class Campfire(Object):
    def __init__(self, player):
        super().__init__("󰻝", "Campfire", solid=True)
        self.player = player

    def interact(self):
        if self.player:
            self.player.hc = self.player.max_hc
            notification_alert.alert("You rested at the campfire and your health was fully restored!")


class Chest(Object):
    def __init__(self):
        super().__init__("󰜦", "Chest", solid=True)

    # def interact(self):


class CraftingTableObject(Object):
    def __init__(self):
        super().__init__("󰖼", "Crafting Table", solid=True)
    
    def interact(self):
        from __main__ import toggle_crafting_table_visibility
        toggle_crafting_table_visibility()


class ObjectManager:
    def __init__(self, player):
        self.player = player
        self.object_list = {}
        self.object_map = {
            "#": Wall(),
            "D": DoorObject("Room2"),
            "󰻝": Campfire(self.player),
            "󰖼": CraftingTableObject(),
            "󰜦": Chest(),
        }

    def get_object(self, char: str):
        class_to_return = self.object_map.get(char)
        return class_to_return

    # def get_object(self, char: str, y: int, x: int):
    #     # we should save room_id as well as the object position
    #     class_to_return = self.object_map.get(char)
    #     if class_to_return not in self.object_list:
    #         self.object_list[(y, x)] = class_to_return
