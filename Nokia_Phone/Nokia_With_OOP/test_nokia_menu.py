import unittest
from nokia_menu import MenuItem, NokiaMenu

class TestNokiaMenu(unittest.TestCase):
    def test_that_selecting_valid_item_returns_submenu(self):
        phone_book = MenuItem("Phone Book", [
            MenuItem("Search"),
            MenuItem("Add Contact")
        ])
        main_menu = MenuItem("Main Menu", [phone_book])
        selected = main_menu.select(1)
        self.assertEqual(selected.name, "Phone Book")

    def test_that_selecting_invalid_item_returns_same_menu(self):
        phone_book = MenuItem("Phone Book", [MenuItem("Search")])
        main_menu = MenuItem("Main Menu", [phone_book])
        selected = main_menu.select(5)
        self.assertEqual(selected, main_menu)

    def test_that_selecting_back_returns_none(self):
        main_menu = MenuItem("Main Menu", [MenuItem("Phone Book")])
        self.assertIsNone(main_menu.select(0))

    def test_that_navigation_into_and_back_works(self):
        phone_book = MenuItem("Phone Book", [MenuItem("Search")])
        main_menu = MenuItem("Main Menu", [phone_book])
        history = []
        current = main_menu
        next_menu = current.select(1)
        history.append(current)
        current = next_menu
        self.assertEqual(current.name, "Phone Book")
        current = history.pop()
        self.assertEqual(current.name, "Main Menu")

    def test_that_nested_submenus_can_be_accessed(self):
        options = MenuItem("Options", [MenuItem("Type of View"), MenuItem("Memory Status")])
        phone_book = MenuItem("Phone Book", [MenuItem("Search"), options])
        main_menu = MenuItem("Main Menu", [phone_book])
        current = main_menu.select(1)
        nested = current.select(2)
        self.assertEqual(nested.name, "Options")

    def test_that_leaf_item_selection_works(self):
        phone_book = MenuItem("Phone Book", [MenuItem("Search")])
        main_menu = MenuItem("Main Menu", [phone_book])
        current = main_menu.select(1)
        leaf = current.select(1)
        self.assertEqual(leaf.name, "Search")

    def test_that_invalid_selection_in_submenu_returns_same_submenu(self):
        phone_book = MenuItem("Phone Book", [MenuItem("Search")])
        main_menu = MenuItem("Main Menu", [phone_book])
        current = main_menu.select(1)
        self.assertEqual(current.select(5), current)

    def test_that_back_in_submenu_returns_none_if_no_history(self):
        phone_book = MenuItem("Phone Book", [MenuItem("Search")])
        main_menu = MenuItem("Main Menu", [phone_book])
        current = main_menu.select(1)
        self.assertIsNone(current.select(0))

    def test_that_multiple_nested_levels_work(self):
        nested = MenuItem("Type of View")
        options = MenuItem("Options", [nested])
        phone_book = MenuItem("Phone Book", [MenuItem("Search"), options])
        main_menu = MenuItem("Main Menu", [phone_book])
        current = main_menu.select(1)
        current = current.select(2)
        current = current.select(1)
        self.assertEqual(current.name, "Type of View")

    def test_that_top_level_item_selection_works(self):
        phone_book = MenuItem("Phone Book")
        messages = MenuItem("Messages")
        main_menu = MenuItem("Main Menu", [phone_book, messages])
        selected = main_menu.select(2)
        self.assertEqual(selected.name, "Messages")

if __name__ == "__main__":
    unittest.main()
