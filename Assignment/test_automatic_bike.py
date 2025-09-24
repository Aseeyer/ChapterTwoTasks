import unittest
from automatic_bike import AutomaticBike, BikeError

class TestAutomaticBike(unittest.TestCase):
    def setUp(self):
        self.bike = AutomaticBike(max_speed=100, fuel_capacity=5.0)

    def test_start_stop(self):
        self.bike.fuel = 1.0
        self.bike.start()
        self.assertTrue(self.bike.engine_on)
        self.assertEqual(self.bike.speed, 0.0)
        self.bike.stop()
        self.assertFalse(self.bike.engine_on)
        self.assertEqual(self.bike.gear, 0)

    def test_cannot_start_without_fuel(self):
        self.bike.fuel = 0.0
        try:
            self.bike.start()
            self.fail("Expected BikeError")
        except BikeError:
            pass

    def test_toggle_lights_and_honk(self):
        self.assertFalse(self.bike.lights_on)
        self.bike.toggle_lights()
        self.assertTrue(self.bike.lights_on)
        self.assertEqual(self.bike.honk(), "Beep!")

    def test_automatic_gear_changes(self):
        self.bike.fuel = 5.0
        self.bike.start()
        self.bike.accelerate(5)
        self.assertEqual(self.bike.gear, 1)
        self.bike.accelerate(10)
        self.assertEqual(self.bike.gear, 2)
        self.bike.accelerate(20)
        self.assertEqual(self.bike.gear, 4)

    def test_braking(self):
        self.bike.fuel = 5.0
        self.bike.start()
        self.bike.accelerate(30)
        self.assertGreater(self.bike.speed, 0)
        self.bike.brake(10)
        self.assertEqual(self.bike.speed, 20)
        self.bike.brake(50)
        self.assertEqual(self.bike.speed, 0)

    def test_manual_mode_shift(self):
        self.bike.fuel = 5.0
        self.bike.start()
        try:
            self.bike.manual_shift(2)
            self.fail("Expected BikeError")
        except BikeError:
            pass
        self.bike.set_mode("manual")
        try:
            self.bike.manual_shift(6)
            self.fail("Expected ValueError")
        except ValueError:
            pass
        self.bike.manual_shift(2)
        self.assertEqual(self.bike.gear, 2)

    def test_accelerate_requires_engine_on(self):
        try:
            self.bike.accelerate(10)
            self.fail("Expected BikeError")
        except BikeError:
            pass
        self.bike.start()
        self.bike.fuel = 0.1
        try:
            self.bike.accelerate(10)
            self.fail("Expected BikeError")
        except BikeError:
            pass

    def test_refuel(self):
        self.bike.fuel = 1.0
        added = self.bike.refuel(2.5)
        self.assertEqual(added, 2.5)
        self.assertAlmostEqual(self.bike.fuel, 3.5)
        added = self.bike.refuel(10)
        self.assertAlmostEqual(self.bike.fuel, self.bike.fuel_capacity)

    def test_run_out_of_fuel_mid_acceleration(self):
        self.bike.fuel = 0.04
        self.bike.start()
        try:
            self.bike.accelerate(10)
            self.fail("Expected BikeError")
        except BikeError:
            pass
        self.assertFalse(self.bike.engine_on)
        self.assertEqual(self.bike.fuel, 0.0)

    def test_max_speed_capping(self):
        self.bike.fuel = 100.0
        self.bike.start()
        self.bike.accelerate(200)
        self.assertEqual(self.bike.speed, float(self.bike.max_speed))

    def test_pull_clutch_and_shift(self):
        self.bike.fuel = 5.0
        self.bike.start()
        self.bike.pull_clutch_and_shift(3)
        self.assertEqual(self.bike.gear, 3)
        try:
            self.bike.pull_clutch_and_shift(10)
            self.fail("Expected ValueError")
        except ValueError:
            pass

if __name__ == "__main__":
    unittest.main()
