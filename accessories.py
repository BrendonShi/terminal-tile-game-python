from item import Item


class AccessoriesHolder:
    def __init__(self, ring = None, necklace = None, gloves = None):
        self.ring = ring
        self.necklace = necklace
        self.gloves = gloves
        
    def add_accessory(self, accessory):
        if isinstance(accessory, Ring):
            self.ring = accessory
        elif isinstance(accessory, Necklace):
            self.necklace = accessory
        elif isinstance(accessory, Gloves):
            self.gloves = accessory
        else:
            print("Wrong accessory type")

    def show_accessories(self):
        print("Ring:", self.ring.name if self.ring else "None")
        print("Necklace:", self.necklace.name if self.necklace else "None")
        print("Gloves:", self.gloves.name if self.gloves else "None")


class Accessory(Item):
    def __init__(self, id: int, name: str, count: int, description: str, accessory_type: str):
        super().__init__(id, name, count, description)
        self.accessory_type = accessory_type


class Ring(Accessory):
    def __init__(self, id: int, name: str, count: int, description: str):
        super().__init__(id, name, count, description, "Ring")


class Necklace(Accessory):
    def __init__(self, id: int, name: str, count: int, description: str):
        super().__init__(id, name, count, description, "Necklace")


class Gloves(Accessory):
    def __init__(self, id: int, name: str, count: int, description: str):
        super().__init__(id, name, count, description, "Gloves")