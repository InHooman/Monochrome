import tkinter as tk
from tkinter import ttk, messagebox
import subprocess


# Function to display the entered wavelength
def display_wavelength():
    entered_value = wavelength_entry.get()
    print(entered_value)  # Or update a label or message box in the GUI


# Function to update the scan rate
def update_scan_rate(direction):
    current_index = scan_rate_menu.current()
    newval = ""
    if direction == "up" and current_index < len(scan_rate_menu["values"]) - 1:
        newval = current_index + 1
    elif direction == "down" and current_index > 0:
        newval = current_index - 1
    scan_rate_menu.current(newval)
    scan_speed_text.set(str(scan_rate_menu.get()))


# Function to display the entered scan speed
def display_scan_speed():
    entered_speed = scan_speed_entry.get()
    print(entered_speed)  # Or update a label or message box in the GUI


# Function to read from grating.conf and update the grating combobox selection
def scan_grating():
    try:
        with open("grating.conf", "r") as file:
            grating_name = file.read().strip()
            grating_index = grating_values.index(grating_name)
            grating_menu.current(grating_index)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read grating.conf: {e}")
        grating_menu.current(0)  # Set to the first item as default if error


# Function to write to running.conf and run motor.py
def write_to_file_and_run_motor(data):
    with open("running.conf", "w") as file:
        for key, value in data.items():
            file.write(f"{key}={value}\n")
    subprocess.run(["python", "motor.py"])


# Area 1 - Wavelength Go Action
def go_action():
    wavelength = wavelength_entry.get()
    data = {"wavelength": wavelength, "mode": "goto"}
    write_to_file_and_run_motor(data)


# Area 2 - Jog Action
def jog_action():
    scan_rate = scan_rate_menu.get()
    scan_speed = scan_speed_entry.get()
    if not scan_speed:
        scan_speed = scan_rate
    data = {"scan_rate": scan_rate, "scan_speed": scan_speed, "mode": "jog"}
    write_to_file_and_run_motor(data)


# Area 4 - Start Scan Action
def start_scan_action():
    start_wavelength = start_wavelength_entry.get()
    end_wavelength = end_wavelength_entry.get()
    scan_speed = scan_speed_entry.get()
    number_of_scans = number_of_scans_entry.get()
    scan_delay = scan_delay_entry.get()
    data = {
        "start_wavelength": start_wavelength,
        "end_wavelength": end_wavelength,
        "scan_speed": scan_speed,
        "number_of_scans": number_of_scans,
        "scan_delay": scan_delay,
        "mode": "scan",
    }
    write_to_file_and_run_motor(data)


# Setting up the main window
root = tk.Tk()
root.title("Operation")

# Dictionary to hold the entry widgets associated with their config_dict names
entries = {}

# Area 1 - Wavelength
wavelength_frame = tk.LabelFrame(root, text="Wavelength")
wavelength_frame.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
tk.Label(wavelength_frame, text="Go to Wavelength").grid(row=0, column=0, sticky="w")
wavelength_entry = tk.Entry(wavelength_frame)
wavelength_entry.grid(row=0, column=1, padx=5, pady=5)
go_button = tk.Button(wavelength_frame, text="Go", command=go_action)
go_button.grid(row=0, column=2, padx=5, pady=5)

# Area 2 - Jog
jog_frame = tk.LabelFrame(root, text="Jog")
jog_frame.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
tk.Label(jog_frame, text="Scan Rate").grid(row=0, column=0, sticky="w")
tk.Label(jog_frame, text="Scan Speed").grid(row=1, column=0, sticky="w")
scan_rate_var = tk.StringVar(value="50")
scan_rate_menu = ttk.Combobox(
    jog_frame, textvariable=scan_rate_var, values=[str(n) for n in range(50, 160, 10)]
)
scan_rate_menu.grid(row=0, column=1, padx=5, pady=5)
tk.Button(jog_frame, text="Up", command=lambda: update_scan_rate("up")).grid(
    row=0, column=2, padx=5, pady=5
)
tk.Button(jog_frame, text="Down", command=lambda: update_scan_rate("down")).grid(
    row=0, column=3, padx=5, pady=5
)
scan_speed_text = tk.StringVar()
scan_speed_entry = tk.Entry(jog_frame, textvariable=scan_speed_text)
scan_speed_entry.grid(row=1, column=1, padx=5, pady=5)
jog_button = tk.Button(jog_frame, text="Jog", command=jog_action)
jog_button.grid(row=1, column=2, padx=5, pady=5)

# Area 3 - Grating
grating_frame = tk.LabelFrame(root, text="Grating")
grating_frame.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
grating_values = [
    "Grating One",
    "Grating Two",
    "Grating Three",
    "Grating Four",
    "Grating Five",
    "Grating Six",
]
grating_menu = ttk.Combobox(grating_frame, values=grating_values)
grating_menu.grid(row=0, column=0, padx=5, pady=5)
scan_button = tk.Button(grating_frame, text="Scan", command=scan_grating)
scan_button.grid(row=0, column=1, padx=5, pady=5)

# Area 4 - Scan
scan_frame = tk.LabelFrame(root, text="Scan")
scan_frame.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
start_wavelength_entry = tk.Entry(scan_frame)
end_wavelength_entry = tk.Entry(scan_frame)
scan_speed_entry = tk.Entry(scan_frame)
number_of_scans_entry = tk.Entry(scan_frame)
scan_delay_entry = tk.Entry(scan_frame)
labels = [
    "Start Wavelength",
    "End Wavelength",
    "Scan Speed",
    "Number of Scans",
    "Scan Delay",
]
entries = [
    start_wavelength_entry,
    end_wavelength_entry,
    scan_speed_entry,
    number_of_scans_entry,
    scan_delay_entry,
]

for i, label in enumerate(labels):
    tk.Label(scan_frame, text=label).grid(row=i, column=0, padx=5, pady=2, sticky="w")
    entries[i].grid(row=i, column=1, padx=5, pady=2)

start_scan_button = tk.Button(scan_frame, text="Start Scan", command=start_scan_action)
start_scan_button.grid(
    row=len(labels), column=0, columnspan=2, sticky="ew", padx=5, pady=5
)

# Run the main loop
root.mainloop()
