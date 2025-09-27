import unittest
from nokia_menu import Menu, MenuItem

class TestNokiaMenu(unittest.TestCase):
    def test_main_menu_display(self):
        menu = Menu("Main Menu")
        menu.add_item(MenuItem("Phone book"))
        menu.add_item(MenuItem("Messages"))
        menu.add_item(MenuItem("Chat"))

        output = menu.display()
        self.assertIn("1. Phone book", output)
        self.assertIn("2. Messages", output)
        self.assertIn("3. Chat", output)

    def test_that_main_menu_display(self):
        menu = Menu("Main Menu")
        menu.add_item(MenuItem("Phone book"))
        menu.add_item(MenuItem("Messages"))
        menu.add_item(MenuItem("Chat"))


if __name__ == "__main__":
    unittest.main()
