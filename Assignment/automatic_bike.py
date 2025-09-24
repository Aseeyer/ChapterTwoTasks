class BikeError(Exception):
    pass

class Camera:
    def __init__(self, darkness=0.3, brake_distance=5.0):
        self.darkness = darkness
        self.brake_distance = brake_distance

    def detect_darkness(self, light_level):
        return light_level < self.darkness

    def detect_close_object(self, distance):
        return distance < self.brake_distance




class AutomaticBike:
    def __init__(self, max_speed=140, fuel_capacity=15.0):
        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity
        self.engine_on = False
        self.speed = 0.0
        self.gear = 0
        self.mode = "automatic"
        self.lights_on = False
        self.horn_sound = "Beep!"
        self.fuel = fuel_capacity
        self._fuel_consumption_per_unit = 0.02

    def start(self):
        if self.fuel <= 0:
            raise BikeError("Cannot start: no fuel.")
        self.engine_on = True
        self.speed = 0.0
        self.gear = 0

    def stop(self):
        self.speed = 0.0
        self.engine_on = False
        self.gear = 0

    def toggle_lights(self):
        self.lights_on = not self.lights_on

    def honk(self):
        return self.horn_sound

    def set_mode(self, mode):
        if mode not in ("automatic", "manual"):
            raise ValueError("Mode must be 'automatic' or 'manual'.")
        self.mode = mode

    def manual_shift(self, gear):
        if self.mode != "manual":
            raise BikeError("Cannot manual shift while in automatic mode.")
        if not self.engine_on:
            raise BikeError("Engine must be on to shift gears manually.")
        if gear < 0 or gear > 5:
            raise ValueError("Gear must be between 0 and 5.")
        self.gear = gear

    def _update_gear_automatic(self):
        s = self.speed
        if not self.engine_on:
            self.gear = 0
        elif s <= 0:
            self.gear = 0
        elif s <= 10:
            self.gear = 1
        elif s <= 25:
            self.gear = 2
        elif s <= 45:
            self.gear = 3
        elif s <= 70:
            self.gear = 4
        else:
            self.gear = 5

    def accelerate(self, delta):
        if delta <= 0:
            raise ValueError("delta must be positive to accelerate.")
        if not self.engine_on:
            raise BikeError("Cannot accelerate: engine is off.")
        if self.fuel <= 0:
            self.stop()
            raise BikeError("Out of fuel - engine stopped.")
        desired = self.speed + delta
        actual_target = min(desired, float(self.max_speed))
        fuel_needed = (actual_target - self.speed) * self._fuel_consumption_per_unit
        if fuel_needed <= self.fuel:
            self.speed = actual_target
            self.fuel -= fuel_needed
        else:
            possible_delta = self.fuel / self._fuel_consumption_per_unit
            self.speed = min(self.speed + possible_delta, float(self.max_speed))
            self.fuel = 0.0
            self.stop()
            raise BikeError("Ran out of fuel during acceleration; engine stopped.")
        if self.mode == "automatic":
            self._update_gear_automatic()

    def brake(self, delta):
        if delta <= 0:
            raise ValueError("delta must be positive to brake.")
        self.speed = max(0.0, self.speed - delta)
        if self.mode == "automatic":
            self._update_gear_automatic()
        if self.speed == 0 and not self.engine_on:
            self.gear = 0

    def refuel(self, liters):
        if liters <= 0:
            raise ValueError("liters must be positive to refuel.")
        space = self.fuel_capacity - self.fuel
        added = min(space, liters)
        self.fuel += added
        return added

    def pull_clutch_and_shift(self, gear):
        if not self.engine_on:
            raise BikeError("Engine must be on to shift gears.")
        if gear < 0 or gear > 5:
            raise ValueError("Gear must be between 0 and 5.")
        self.gear = gear

    def auto_lights(self, camera, light_level):
        if camera.detect_darkness(light_level):
            self.lights_on = True
            print("Automatic: Lights turned ON due to darkness.")
        else:
            self.lights_on = False
            print("Automatic: Lights turned OFF, it's bright enough.")

    def auto_brake(self, camera, distance):
        if camera.detect_close_object(distance):
            self.brake(10)
            print("Automatic: Emergency brake applied! Object too close.")

if __name__ == "__main__":
    my_power_bike = AutomaticBike()
    cam = Camera()

    try:
        my_power_bike.start()
        print("Bike started. Engine on:", my_power_bike.engine_on)

        my_power_bike.auto_lights(cam, light_level=0.2)

        my_power_bike.accelerate(20)
        print(f"Speed after accelerating: {my_power_bike.speed} km/h")
        print(f"Current gear: {my_power_bike.gear}")
        print(f"Fuel left: {my_power_bike.fuel:.2f} L")

        my_power_bike.auto_brake(cam, distance=3)

        my_power_bike.toggle_lights()
        print("Lights on:", my_power_bike.lights_on)

        print("Horn sound:", my_power_bike.honk())

        my_power_bike.brake(5)
        print(f"Speed after braking: {my_power_bike.speed} km/h")
        print(f"Current gear: {my_power_bike.gear}")

        my_power_bike.stop()
        print("Bike stopped. Engine on:", my_power_bike.engine_on)

    except BikeError as e:
        print("Bike error:", e)
    except Exception as e:
        print("Other error:", e)
