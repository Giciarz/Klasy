class Machine:
    def __init__(self, frequency, power, voltage, calibration, number_of_turns, type_of_power):
        self.frequency = frequency
        self.power = power
        self.voltage = voltage
        self.__calibration = calibration
        self.__number_of_turns = number_of_turns
        self.__type_of_power = type_of_power

    def __set_number_of_turns(self, number):
        self.__number_of_turns = int(number)
        return number

    def __set_type_of_power(self, type_of):
        self.__type_of_power = str(type_of)
        return type_of

    def set_calibration(self, number, type_of):
        self.__calibration = True
        self.__number_of_turns(number)
        self.__type_of_power(type_of)
        return number, type_of

    def set_power(self, value):
        self.set_power = int(value)
