import unittest
from nokia_menu import Menu, MenuItem

class TestNokiaMenu(unittest.TestCase):
    def test_that_menu_display_shows_all_items(self):
        menu = Menu("Main Menu")
        menu.add_item(MenuItem("Phone book"))
        menu.add_item(MenuItem("Messages"))
        menu.add_item(MenuItem("Chat"))

        output = menu.display()
        self.assertIn("1. Phone book", output)
        self.assertIn("2. Messages", output)
        self.assertIn("3. Chat", output)

    def test_that_menu_selection_returns_correct_item(self):
        menu = Menu("Main Menu")
        menu.add_item(MenuItem("Phone book"))
        menu.add_item(MenuItem("Messages"))

        selected = menu.select(1)
        self.assertEqual(selected.title, "Phone book")

if __name__ == "__main__":
    unittest.main()
