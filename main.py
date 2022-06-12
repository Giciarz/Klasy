from methods import Machine


def main():

    big_machine = Machine(None, None, None, None, None, None)
    big_machine.frequency = int(input("Frequency: \n"))
    big_machine.power = int(input("Power: \n"))
    big_machine.voltage = int(input("Voltage: \n"))
    # big_machine.calibration ?!
    big_machine.number_of_turns = int(input("Number of turns: \n"))
    big_machine.type_of_power = str(input("Type of power: "))

    print(f"""
    Frequency: {big_machine.frequency}
    Power: {big_machine.power}
    Voltage: {big_machine.voltage}
    Number of turns: {big_machine.number_of_turns}
    Type of power: {big_machine.type_of_power}
    """)


if __name__ == '__main__':
    main()
