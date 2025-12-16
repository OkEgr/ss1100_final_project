from command_dict import command_dict

def parse_command(command_string):
    """
    Parses a command string and returns a tuple with the full subsystem name,
    the command description, and the parameter value.
    """
    """
    The following code was created by ChatGPT by copying in the commands and the dictionary.
    ChatGPT asked if I wanted a command parser. I briefly tried adding error checking by hand and 
    then ended up adding most of that in with ChatGPT as well. A few outputs had to be adjusted by hand to match
    the expected outputs for the test scripts. Error checking for missing colon was added in as well.
    """
    try:
        code, cmd_key, value_str = command_string.split(":")
    except ValueError:
        print("INVALID COMMAND - Improper format")
        return None, None, None
    # Check for non-integer string for value when converting to int
    try:
        value = int(value_str)
    except ValueError:
        print("INVALID COMMAND - Non-integer value")
        return None, None, None

    # Find subsystem by code
    subsystem_data = None
    subsystem_name = None
    for name, data in command_dict.items():
        if data["Code"] == code:
            subsystem_data = data
            subsystem_name = name
            break

    if subsystem_data is None:
        print({"Error": f"Subsystem code '{code}' not found."})
        return None, None, None

    # Check if command key exists
    commands = subsystem_data.get("Commands", {})
    if cmd_key not in commands:
        print({"Error": f"Command '{cmd_key}' not found in subsystem '{subsystem_name}'."})
        return None, None, None

    # Extract command info
    command_name, allowed_values = commands[cmd_key]

    # Optionally, check if input value is allowed
    if (isinstance(allowed_values, set) and value not in allowed_values) or \
       (hasattr(allowed_values, "__contains__") and value not in allowed_values):
        print({"Error": f"Value '{value}' is outside of tolerances allowed in '{subsystem_name}'."})
        return None, None, None
    return (
        subsystem_name,
        command_name,
        value
    ) # this is a single tuple as the return, rather than three individual objects being returned


def main():
    """
    Main function to test the command parser.
    """
    test_commands = [
        "EPS:CMD01:0",
        "ACS:CMD04:-1",
        "RCS:INVALID:0",
    ]

    for cmd in test_commands:
        subsystem, description, value = parse_command(cmd)
        print(f"Command: {cmd}")
        print(f" -> Subsystem: {subsystem}")
        print(f" -> Description: {description}")
        print(f" -> Value: {value}")
        print("-" * 20)

if __name__ == "__main__":
    main()
