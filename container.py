import copy
from alert import notification_alert

from item import Item, UsefulItems, Stick, Wood, WoodenSword, BlueMango, MoonFlower, RedMoonFlower, MonsterEye
from potion import HealthPotion, ManaPotion


class Container:
    def __init__(self, name: str):
        self.name = name
        self.items = {}
        self.is_focused = False
        self.chosen_item = 0

    def __getitem__(self, key):
        return self.items.get(key, 0)

    def fix_indicator(self, item):
        # if item.id in self.items and self.items[item.id].count == 1:
        #     if self.chosen_item == len(self.items.keys())-1:
        #         self.chosen_item = len(self.items.keys())-2
        #     else:
        #         self.chosen_item

        # if item.id in self.items and self.items[item.id].count == 1:
        #     if self.chosen_item == len(self.items.keys())-1:
        #         self.chosen_item = len(self.items.keys())-2
        if self.chosen_item >= len(self.items):
            self.chosen_item = len(self.items)-1


    def get_chosen_item(self):
        item_ids = list(self.items.keys())
        if self.chosen_item != -1 and self.chosen_item < len(item_ids):
            selected_id = item_ids[self.chosen_item]
            item = copy.deepcopy(self.items[selected_id])
            item.count = 1
            return item

    def transfer_item(self, container):
        item = self.get_chosen_item()
        if item:
            container.add_item(item)
            self.remove_item(item)
            self.fix_indicator(item)
        else:
            print("No item was chosen")

    def add_item(self, item: Item):
        if item.id in self.items:
            #self.items[item.id].count += 1
            self.items[item.id].count += item.count
        else:
            self.items[item.id] = item

    def remove_item(self, item, amount=1):
        if item.id in self.items and self.items[item.id].count >= amount:
            self.items[item.id].count -= amount
            if self.items[item.id].count <= 0:
                del self.items[item.id]
        else:
            print(f"Item '{item}' not found in Inventory")

    def show_items(self):
        name: int = round((26 - len(self.name))/2)
        name_to_display = name*" " + self.name + name*" "

        is_even = len(self.name) % 2
        if is_even == 1:
            name_to_display += " "
        if not self.items:
            x_element = " "
            if self.is_focused:
                x_element = "x"
            print("┌──────────────────────────┐")
            print(f"│{name_to_display}│")
            print("├──────────────────────────┤")
            print(f"│ {x_element} No Items in Inventory  │")
            print("└──────────────────────────┘")
        else:
            item_keys = list(self.items.keys())
            
            print("┌──────────────────────────┐")
            print(f"│{name_to_display}│")
            print("├──────────────────────────┤")

            for index, item_id in enumerate(item_keys):
                item = self.items[item_id]
                
                is_chosen = index == self.chosen_item
                indicator = ">" if is_chosen and self.is_focused else " "

                content = f"{item.icon} {item.name}: {item.count}"
                
                add_lenght = len(item.name) + len(str(item.count))
                padded_content = content + (18-add_lenght)*" "
                
                print(f"│ {indicator} {padded_content} │")

            print("└──────────────────────────┘")

    def move_up(self):
        item_ids = list(self.items.keys())
        if not item_ids:
            return

        if self.chosen_item > 0:
            self.chosen_item -= 1
        else:
            print("Can't move up more")

    def move_down(self):
        item_ids = list(self.items.keys())
        if not item_ids:
            return

        if self.chosen_item < len(item_ids) - 1:
            self.chosen_item += 1
        else:
            print("Can't move down more")


class Inventory(Container):
    def __init__(self):
        super().__init__("Inventory")

    def select_item(self, player):
        item = self.get_chosen_item()
        if item:
            item.use(player)
            self.fix_indicator(item)
            # should delete item here (maybe | not sure)
        else:
            print("No selected item")


class CraftingTable(Container):
    from item import UsefulItems
    def __init__(self):
        super().__init__("Crafting Table")

    def _get_items_by_name(self):
        items_by_name = {}
        for item in self.items.values():
            items_by_name[item.name] = item.count
        return items_by_name

    def craft(self, recipes, player):
        items_in_crafting_table = self._get_items_by_name()
        for recipe_name, required_ingredients in recipes.items():
            #if len(items_in_crafting_table) != len(required_ingredients):
            #    continue

            is_a_match = True
            for ingredient_name, required_amount in required_ingredients.items():
                if items_in_crafting_table.get(ingredient_name) != required_amount:
                    is_a_match = False
                    break 
            
            if is_a_match:
                crafted_item = UsefulItems.create_item_instance(recipe_name)
                if crafted_item:
                    notification_alert.alert(f"You have crafted a {crafted_item.name}!")
                    player.inventory.add_item(crafted_item)
                    self.items.clear()
                    return
                else:
                    notification_alert.alert(f"(!) Error: No item class found for recipe name '{recipe_name}'.")
                    return

        notification_alert.alert("Cannot craft anything")
