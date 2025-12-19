from typing import Dict, List
from load_rooms import RoomLoader
import random


roomloader = RoomLoader()


class Room:
    def __init__(self, terrain: str):
        self.objects: Dict[tuple, Object] = {}
        self.terrain = terrain

    def add_object(self, coordinates, given_object):
        self.objects[coordinates] = given_object

    def __str__(self):
        return self.terrain

    def __repr__(self):
        # A more descriptive repr is helpful for debugging
        return f"Room(terrain='{self.terrain[:20]}...')"


class RoomManager:
    def __init__(self):
        self.rooms: Dict[int, Room] = {}
        self.next_room_id_num = 0
        self.current_room = -1
        self.loader = roomloader
        self.loader.load_rooms()

    def get_loader_list(self):
        all_room_data_lists = self.loader.room_list.values()
        if not all_room_data_lists:
            raise ValueError("can't get room data.")

        loader_all_rooms = [
            room_data for sublist in all_room_data_lists for room_data in sublist
        ]

        return loader_all_rooms

    def get_random_room(self):
        flat_list_of_all_rooms = self.get_loader_list()
        if flat_list_of_all_rooms:
            random_room_data = random.choice(flat_list_of_all_rooms)
            return random_room_data.text

    def generate_random_room(self) -> Room:
        room_terrain = self.get_random_room()

        generated_room_id = self.next_room_id_num
        self.current_room = self.next_room_id_num
        self.next_room_id_num += 1

        room = Room(terrain=room_terrain)
        self.rooms[generated_room_id] = room
        # return room

    # def generate_start_room(self) -> Room:
    #     all_loaded_rooms = self.get_loader_list()
    #     if all_loaded_rooms:
    #         room_terrain = all_loaded_rooms[0]

    #     generated_room_id = self.next_room_id_num
    #     self.current_room = self.next_room_id_num
    #     self.next_room_id_num += 1

    #     room_terrain_text = room_terrain.text
    #     room = Room(terrain=room_terrain_text)
    #     self.rooms[generated_room_id] = room

    def generate_start_room(self) -> Room:
        all_loaded_rooms = self.get_loader_list()

        if not all_loaded_rooms:
            raise ValueError("no rooms were loaded.")

        room_terrain_data = all_loaded_rooms[0]
        room_terrain_text = room_terrain_data.text

        generated_room_id = self.next_room_id_num
        self.current_room = generated_room_id
        self.next_room_id_num += 1

        room = Room(terrain=room_terrain_text)
        self.rooms[generated_room_id] = room
        return room

    def get_current_room(self) -> Room:
        if self.current_room in self.rooms:
            return self.rooms[self.current_room]