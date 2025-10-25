import unittest
from fuel_system import Fuel
from dispenser_machine import DispenserMachine

class TestFuel(unittest.TestCase):
    def setUp(self):
        self.petrol = Fuel("Petrol", 650.0, 1000)

    def test_get_name_returns_correct_value(self):
        self.assertEqual(self.petrol.get_name(), "Petrol")

    def test_get_price_per_unit_returns_correct_value(self):
        self.assertEqual(self.petrol.get_price_per_unit(), 650.0)

    def test_get_available_quantity_returns_correct_value(self):
        self.assertEqual(self.petrol.get_available_quantity(), 1000)

    def test_dispense_reduces_quantity_when_enough_available(self):
        check = self.petrol.dispense(100)
        self.assertTrue(check)
        self.assertEqual(self.petrol.get_available_quantity(), 900)

    def test_dispense_returns_false_when_quantity_too_large(self):
        check = self.petrol.dispense(2000)
        self.assertFalse(check)
        self.assertEqual(self.petrol.get_available_quantity(), 1000)

    def test_dispense_returns_false_for_negative_quantity(self):
        success = self.petrol.dispense(-10)
        self.assertFalse(success)
        self.assertEqual(self.petrol.get_available_quantity(), 1000)

    def test_get_cost_calculates_correctly(self):
        cost = self.petrol.get_cost(5)
        self.assertEqual(cost, 3250.0)

    def test_get_cost_returns_zero_for_invalid_quantity(self):
        cost = self.petrol.get_cost(-2)
        self.assertEqual(cost, 0)

    def test_update_price_changes_price_when_valid(self):
        success = self.petrol.update_price(700.0)
        self.assertTrue(success)
        self.assertEqual(self.petrol.get_price_per_unit(), 700.0)

    def test_update_price_returns_false_for_invalid_price(self):
        success = self.petrol.update_price(10)
        self.assertFalse(success)
        self.assertEqual(self.petrol.get_price_per_unit(), 650.0)

