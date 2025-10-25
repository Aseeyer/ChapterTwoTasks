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
