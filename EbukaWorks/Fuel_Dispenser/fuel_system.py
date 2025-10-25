class Fuel:
    def __init__(self, name, price_per_unit, initial_quantity):
        self.__name = name
        self.__price_per_unit = price_per_unit
        self.__available_quantity = initial_quantity

    def get_name(self):
        return self.__name

    def get_price_per_unit(self):
        return self.__price_per_unit

    def get_available_quantity(self):
        return self.__available_quantity

    def dispense(self, quantity):
        if quantity <= 0:
            return False
        if quantity > self.__available_quantity:
            return False
        self.__available_quantity -= quantity
        return True

    def get_cost(self, quantity):
        if quantity <= 0:
            return 0
        return quantity * self.__price_per_unit

