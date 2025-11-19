def available_power(voltage, current):
    """
    Calculates the instantaneous incoming power from the solar panels,
    checking for inputs that exceed the solar panels' maximum limits.
    """
    if voltage > 28:
        voltage = 28
    if current > 10:
        current = 10
    power = voltage*current
    return power

def battery_charging(power_delivered, time_elapsed):
    """
    Calculates the total energy available for battery charging.
    """
    energy = power_delivered*time_elapsed
    return energy
def total_energy(power_data):
    """
    Calculates the total energy available for battery charging across a data set of different
    power availability over time.
    """
    # Check plus code
    total = 0
    for i, (v, i_current, t) in enumerate(power_data):
        power = available_power(v, i_current)
        energy = battery_charging(power, t)
        total += energy
    return total

def main():
    """
    Main function to test the EPS functions.
    """
    # Example test cases from the project description
    test_cases = [
        (25, 10, 3600),
        (30, 8, 1800),
        (15, 12, 7200)
    ]
    new_test_case1 = [(22,7,300), (40,7,60), (25,10,200), (10,4,600)]
    new_test_case2 = [(0,7,300), (30,10,60), (28,10,200), (10,10,10)]


    for i, (v, i_current, t) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        power = available_power(v, i_current)
        print(f"Available Power: {power:.2f} W")
        energy = battery_charging(power, t)
        print(f"Energy for charging: {energy:.2f} J")
        print("-" * 20)

    # Test check plus function
    print(f"--- Test Case Check Plus 1 ---")
    available_energy = total_energy(new_test_case1)
    print(f"Total Energy Stored: {available_energy:.2f} J")
    print("-" * 20)

    print(f"--- Test Case Check Plus 2 ---")
    available_energy = total_energy(new_test_case2)
    print(f"Total Energy Stored: {available_energy:.2f} J")
    print("-" * 20)

if __name__ == "__main__":
    main()
