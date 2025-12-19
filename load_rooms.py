import os
from typing import Dict, List


class RoomData:
    def __init__(self, text, doors):
        self.text = text
        self.doors = doors

    def __str__(self):
        return self.text

    def __repr__(self):
        # return f"RoomData(doors={self.doors})"
        return self.text


class RoomLoader:
    door_symbols = ["S", "N", "W", "E", "A", "B", "C"]

    def __init__(self):
        self.room_list: Dict[str, List[RoomData]] = {}

    def load_rooms(self):
        rooms_folder = os.path.join(os.getcwd(), 'rooms')
        if not os.path.isdir(rooms_folder):
            return

        all_room_files = os.listdir(rooms_folder)

        for room_file in all_room_files:
            room_path = os.path.join(rooms_folder, room_file)
            try:
                with open(room_path, "r", encoding="utf-8") as f:
                    room_file_text = f.read()
                    self.process_room(room_file_text)
            except Exception as e:
                print(f"Could not read file {room_file}: {e}")

    def process_room(self, room_text: str):
        doors_found = set()
        for char in room_text:
            if char in self.door_symbols:
                doors_found.add(char)

        if not doors_found:
            return

        room_data = RoomData(room_text, list(doors_found))

        for door in doors_found:
            if door not in self.room_list:
                self.room_list[door] = []
            self.room_list[door].append(room_data)

    def get_rooms_with_door(self, symbol: str) -> List[RoomData]:
        return self.room_list.get(symbol, [])