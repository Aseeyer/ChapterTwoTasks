import unittest
from nokia_menu import Menu, MenuItem

class TestNokiaMenu(unittest.TestCase):
    def test_that_menu_display_shows_all_items(self):
        main_menu = Menu("Main Menu")
        main_menu.add_item(MenuItem("Phone book"))
        main_menu.add_item(MenuItem("Messages"))
        main_menu.add_item(MenuItem("Chat"))

        output = main_menu.display()
        self.assertIn("1. Phone book", output)
        self.assertIn("2. Messages", output)
        self.assertIn("3. Chat", output)

    def test_that_menu_selection_returns_correct_item(self):
        main_menu = Menu("Main Menu")
        main_menu.add_item(MenuItem("Phone book"))
        main_menu.add_item(MenuItem("Messages"))

        selected_item = main_menu.select(1)
        self.assertEqual(selected_item.title, "Phone book")

if __name__ == "__main__":
    unittest.main()
