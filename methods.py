
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

    def __set_type_of_power(self, type_of):
        self.__type_of_power = type_of

    def set_calibration(self):
        self.__calibration = True
        return self.__number_of_turns, self.__type_of_power, self.__calibration

    def set_power(self, value):
        self.power = value

    def set_voltage(self, volt):
        self.voltage = volt

    def get_power(self):
        return self.power

    def get_voltage(self):
        return self.voltage
