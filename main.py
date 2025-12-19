import keyboard
import threading
import os
import platform
from player import Player
from tileset import TileSet
from potion import HealthPotion, ManaPotion
from item import Item, Stick, Wood, WoodenSword, BlueMango, MoonFlower, RedMoonFlower, MonsterEye
from container import CraftingTable, Inventory
from container_manager import ContainerManager
import json
from object import ObjectManager
from alert import notification_alert
# from load_rooms import RoomLoader
from roommanager import RoomManager

stop_event = threading.Event()


player = Player("Franko", 1, 3, 1, 2)

player.position.y = 3
player.position.x = 10

player.inventory.add_item(HealthPotion(6))
player.inventory.add_item(Wood(6))
player.inventory.add_item(Stick(4))
player.inventory.add_item(ManaPotion(1))
player.inventory.add_item(ManaPotion(2))
player.inventory.add_item(BlueMango(20))
player.inventory.add_item(MoonFlower(20))

crafting_table = CraftingTable()
container_manager = ContainerManager()
container_manager.add_container(player.inventory)


# roomloader = RoomLoader()
# roomloader.load_rooms()

roommanager = RoomManager()

first_room = roommanager.generate_start_room()
roomlines = (str(first_room)).splitlines()
# _ old | new ^
# roommanager.generate_start_room()
# roomlines = (str(roommanager.get_current_room())).splitlines()

#
current_dir = os.path.dirname(os.path.abspath(__file__))
# room_file = os.path.join(current_dir, 'rooms', 'room1.txt')

# with open(room_file, "r", encoding="utf8") as f:
#     room = f.read()
# ^
# roomlines = room.splitlines()


tileset = TileSet()
map = tileset.get_tiles(roomlines)

recipes_file = os.path.join(current_dir, 'recipes.json')
with open(recipes_file, "r") as file:
    recipes = json.load(file)

object_manager = ObjectManager(player)

def check_for_interaction(y: int, x: int):
    if not (0 <= y < len(roomlines) and 0 <= x < len(roomlines[0])):
        return None

    char = roomlines[y][x]
    obj = object_manager.get_object(char)

    if obj:
        # if obj.solid:
        #     return None
        # else:
        #     return obj
        return obj

    return None


def print_screen():
    clear_screen()
    print_map() 
    print_player()
    print_containers()
    notification_alert.display_alert()


# ??? need to cache this in room class, too much overhead
def print_map():
    for y in range(len(map)):
        line = ""
        for x in range(len(map[y])):
            if x == player.position.x and y == player.position.y:
                line += "i"
            elif map[y][x] == " ":
                line += "\033[38;5;239m⬝\033[0m"
            else:
                line += map[y][x]
        print(line)


def clear_screen():
    os_name = platform.system()
    
    if os_name == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def print_containers():
    containers = container_manager.opened_containers
    for container in containers:
        container.show_items()

def toggle_crafting_table_visibility():
    global container_visibility
    if not crafting_table in container_manager.opened_containers:
        container_manager.add_container(crafting_table)
    else:
        container_manager.remove_container(crafting_table)


def print_player():
    print("\n\n\n")
    player.show_stats()


def move_player(move_x, move_y):
    new_y = player.position.y + move_y
    new_x = player.position.x + move_x

    target = check_for_interaction(new_y, new_x)

    if target:
        target.interact()
        if target.solid:
            return
    player.position.y = new_y
    player.position.x = new_x

    remove_any_container()  # useless


def remove_any_container():  # useless
    if crafting_table in container_manager.opened_containers:  # useless
        container_manager.remove_container(crafting_table)  # useless


def player_actions(event):
    if event.name == "q":
        stop_event.set()
        return

    # make it with signals? So mobs and objects can know you're moving
    if event.name == 'w':
        move_player(0, -1)
    elif event.name == "s":
        move_player(0, 1)
    elif event.name == "d":
        move_player(1, 0)
    elif event.name == "a":
        move_player(-1, 0)

    elif event.name == "up":
        container_manager.get_current_container().move_up()

    elif event.name == "down":
        container_manager.get_current_container().move_down()

    elif event.name == "right":
        current_container = container_manager.get_current_container()
        next_container_index = container_manager.opened_containers.index(current_container) + 1
        if next_container_index >= len(container_manager.opened_containers):
            next_container_index = 0
        next_container = container_manager.opened_containers[next_container_index]
        current_container.transfer_item(next_container)

    elif event.name == "enter":
        current_container = container_manager.get_current_container()
        if isinstance(current_container, Inventory):
            player.inventory.select_item(player)

    elif event.name == "left":
        container_manager.switch_container()

    # elif event.name == "c":
    #     toggle_crafting_table_visibility()

    elif event.name == ".":
        if crafting_table in container_manager.opened_containers:
            crafting_table.craft(recipes, player)

    elif event.name == "esc":
        notification_alert.clear_alert()

    print_screen()


def game_loop():
    while True:
        keyboard.on_press(player_actions)

        stop_event.wait()
        
        keyboard.unhook_all()
        break


if __name__ == "__main__":
    print_screen()
    game_loop()
