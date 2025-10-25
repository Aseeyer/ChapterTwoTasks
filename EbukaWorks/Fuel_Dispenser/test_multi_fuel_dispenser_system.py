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

    def test_restock_increases_quantity_when_valid(self):
        success = self.petrol.restock(200)
        self.assertTrue(success)
        self.assertEqual(self.petrol.get_available_quantity(), 1200)

    def test_restock_returns_false_for_small_amount(self):
        success = self.petrol.restock(50)
        self.assertFalse(success)
        self.assertEqual(self.petrol.get_available_quantity(), 1000)




class TestDispenserMachine(unittest.TestCase):
    def setUp(self):
        self.petrol = Fuel("Petrol", 650.0, 1000)
        self.diesel = Fuel("Diesel", 550.0, 800)
        self.machine = DispenserMachine({
            "Petrol": self.petrol,
            "Diesel": self.diesel
        })

    def test_get_available_fuels_returns_correct_list(self):
        fuels = self.machine.get_available_fuels()
        self.assertEqual(len(fuels), 2)
        self.assertEqual(fuels[0]["name"], "Petrol")
        self.assertEqual(fuels[1]["name"], "Diesel")

    def test_dispense_fuel_reduces_quantity_and_returns_cost(self):
        cost = self.machine.dispense_fuel("Petrol", 10)
        self.assertEqual(cost, 10 * 650.0)
        self.assertEqual(self.petrol.get_available_quantity(), 990)

    def test_dispense_fuel_returns_error_for_invalid_fuel(self):
        result = self.machine.dispense_fuel("Kerosene", 10)
        self.assertEqual(result, "Fuel not found")

    def test_dispense_fuel_returns_error_for_insufficient_quantity(self):
        result = self.machine.dispense_fuel("Diesel", 900)
        self.assertEqual(result, "Insufficient fuel quantity")

