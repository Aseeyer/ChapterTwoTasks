from fuel_system import Fuel

class DispenserMachine:
    def __init__(self, fuels):
        self.__fuels = fuels

    def get_available_fuels(self):
        return [
            {
                "name": fuel.get_name(),
                "price": fuel.get_price_per_unit(),
                "quantity": fuel.get_available_quantity()
            }
            for fuel in self.__fuels.values()
        ]

    def dispense_fuel(self, fuel_name, quantity):
        if fuel_name not in self.__fuels:
            return "Fuel not found"
        fuel = self.__fuels[fuel_name]
        if fuel.get_available_quantity() < quantity or quantity <= 0:
            return "Insufficient fuel quantity"
        success = fuel.dispense(quantity)
        if success:
            return fuel.get_cost(quantity)
        return "Unable to dispense fuel"

   