import random
import time
import matplotlib.pyplot as plt

target_temp = random.randint(-30, 60)
print(f"Your target temperature for this iteration is {target_temp}")
############ DO NOT EDIT ABOVE THIS LINE ##############################

def process_temperature(input_temp, target_temp):
    """Function that takes an input temperature and target temperature
    applies a function to move it towards equilibrium.
    It should return a single float as the output indicating 
    the new, altered temperature"""
    return 0 # Delete this line and insert your code starting here!


################### DO NOT EDIT BELOW THIS LINE ############################
def plot_results(time_steps, uncontrolled, controlled, target):
    plt.figure(figsize=(10, 6))
    plt.plot(time_steps, uncontrolled, label='Uncontrolled Temperature', linestyle='--')
    plt.plot(time_steps, controlled, label='Controlled Temperature', marker='o')
    plt.axhline(y=target, color='r', linestyle='-', label='Target Temperature')
    plt.title('Temperature Control System Performance')
    plt.xlabel('Time Step')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    duration = 15  # Duration to feed signals in seconds
    uncontrolled_history = []
    controlled_history = []
    time_steps = list(range(duration + 1))

    temperature = random.randint(-30, 60)
    
    for i in time_steps:
        uncontrolled_history.append(temperature)
        print(f"Time {i}: Current temperature reading: {temperature:.2f}°C")
        
        # Student's processing function is called here
        controlled_temp = process_temperature(temperature, target_temp)
        controlled_history.append(controlled_temp)
        print(f"         TCS Action -> New temperature: {controlled_temp:.2f}°C")

        # Simulate the next temperature reading based on some external factors
        direction = random.choice([-1, 1])
        change = random.uniform(0, 5) * direction
        temperature = max(-30, min(60, controlled_temp + change))

        if i < duration:
            time.sleep(1)  # Wait for 1 second before the next signal

    plot_results(time_steps, uncontrolled_history, controlled_history, target_temp)

if __name__ == "__main__":
    main()
#########################################################################
