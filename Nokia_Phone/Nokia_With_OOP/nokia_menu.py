class MenuItem:
    def __init__(self, title):
        self.title = title


class Menu:
    def __init__(self, menu_title):
        self.menu_title = menu_title
        self.menu_items = []

    def add_item(self, menu_item):
        self.menu_items.append(menu_item)

    def display(self):
        output = f"{self.menu_title}:\n"
        for item_number, menu_item in enumerate(self.menu_items, start=1):
            output += f" {item_number}. {menu_item.title}\n"
        return output

    def select(self, item_number):
        if 1 <= item_number <= len(self.menu_items):
            return self.menu_items[item_number - 1]
        return None
