# Function to parse the configuration file
def parse_config():
    config_dict = {}
    with open("running.conf", "r") as file:
        for line in file:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                config_dict[key] = value
    return config_dict


# Function to perform the 'jog' operation
def jog_operation(config_dict):
    # Replace these print statements with actual motor control code
    limit_a = 0  # Define actual limit
    limit_b = 100  # Define actual limit
    speed = float(config_dict.get("scan_speed", 1))  # Use default speed if not specified
    print(f"Jogging from {limit_a} to {limit_b} at speed {speed}")
    # Add motor control logic here


# Function to perform the 'goto' operation
def goto_operation(config_dict):
    # Replace these print statements with actual motor control code
    wavelength = config_dict.get("wavelength")
    default_speed = 1  # Set your default speed
    print(f"Going to wavelength {wavelength} at default speed {default_speed}")
    # Add motor control logic here


# Function to perform the 'scan' operation
def scan_operation(config_dict):
    # Replace these print statements with actual motor control code
    start_wavelength = config_dict.get("start_wavelength")
    end_wavelength = config_dict.get("end_wavelength")
    scan_speed = float(
        config_dict.get("scan_speed", 1)
    )  # Use default speed if not specified
    print(f"Scanning from {start_wavelength} to {end_wavelength} at speed {scan_speed}")
    # Add motor control logic here


# Main logic
if __name__ == "__main__":
    # Parse the configuration file
    config = parse_config()

    # Determine the mode and call the appropriate function
    mode = config.get("mode")
    if mode == "jog":
        jog_operation(config)
    elif mode == "goto":
        goto_operation(config)
    elif mode == "scan":
        scan_operation(config)
    else:
        print("No valid mode found in configuration.")
