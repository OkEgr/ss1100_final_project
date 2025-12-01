# Portions of this code were cleaned up and refined by chatGPT.

MAX_THRUST = 100       # Newtons
MAX_FLOW = 0.05        # kg/s
MAX_VELOCITY = 2000    # m/s
SPACECRAFT_MASS = 500  # kg

def malfunction_detection(thrust_values):
    """
    Checks input thrust values and angles for each thruster against set limits.
    If a thruster is outside of these limits, it prints a message.
    """
    for thruster_name, thrust, flow_rate, exhaust_velocity in thrust_values:
        malfunction = False

        if thrust > MAX_THRUST:
            print(f"[!] {thruster_name} THRUST TOO HIGH: {thrust} N (exceeds by {thrust - MAX_THRUST} N)")
            malfunction = True

        if flow_rate > MAX_FLOW:
            print(f"[!] {thruster_name} FLOW RATE TOO HIGH: {flow_rate} kg/s (exceeds by {flow_rate - MAX_FLOW} kg/s)")
            malfunction = True

        if exhaust_velocity > MAX_VELOCITY:
            print(f"[!] {thruster_name} EXHAUST VELOCITY TOO HIGH: {exhaust_velocity} m/s (exceeds by {exhaust_velocity - MAX_VELOCITY} m/s)")
            malfunction = True

        if not malfunction:
            print(f"{thruster_name}: All parameters within safe limits.")

def velocity_change_calculation(m_dot, v_e, t):
    """
    Performs calculations to determine the change in velocity resulting from a maneuver event.
    """
    thrust = m_dot * v_e
    delta_v = (thrust * t) / SPACECRAFT_MASS
    return delta_v

# Check plus fucntion

def vector_velocity_change(m_dot, v_e, t):
    """
    Calculates delta v vector (dx, dy, dz) for all three thrusters.
    """

    dvx = (m_dot[0] * v_e[0] * t[0]) / SPACECRAFT_MASS
    dvy = (m_dot[1] * v_e[1] * t[1]) / SPACECRAFT_MASS
    dvz = (m_dot[2] * v_e[2] * t[2]) / SPACECRAFT_MASS

    return (dvx, dvy, dvz)

def main():
    """
    Main function to test the RCS functions.
    """
    print("\n--- Malfunction Detection Test ---")
    malfunction_detection([
        ("Thruster 1", 20, 0.02, 1000),
        ("Thruster 2", 120, 0.06, 1000),  # Out of limits
        ("Thruster 3", 80, 0.05, 2500)    # Out of limits
    ])

    print("\n--- Velocity Change Calculation Test ---")
    test_cases = [
        (0.02, 1000, 5),
        (0.06, 1000, 3),
        (0.05, 2000, 10)
    ]

    for i, (m_dot, v_e, t) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        delta_v = velocity_change_calculation(m_dot, v_e, t)
        print(f"Calculated delta_v: {delta_v:.2f} m/s")
        print("-" * 20)

    print("\n--- Vector delta v Calculation ---")
    dv_vector = vector_velocity_change(
        [0.04, 0.03, 0.01],
        [2000, 2000, 2000],
        [15, 4, 3]
    )
    print(f"Vector delta_v (dx, dy, dz): {dv_vector}")

if __name__ == "__main__":
    main()
