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

   