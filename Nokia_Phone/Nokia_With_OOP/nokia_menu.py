class MenuItem:
    def __init__(self, title):
        self.title = title


class Menu:
    def __init__(self, title):
        self.title = title
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display(self):
        output = f"{self.title}:\n"
        for i, item in enumerate(self.items, start=1):
            output += f" {i}. {item.title}\n"
        return output
