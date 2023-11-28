import tkinter as tk


# Function to display the value of the 'Front' entry field
def set_front_slit(slit_type):
    entered_value = front_entries[slit_type].get()
    print(
        f"{slit_type} Front Set to: {entered_value}"
    )  # Placeholder for actual set action


# Function to home the 'Front' slit
def home_front_slit(slit_type):
    print(f"{slit_type} Front Homed")  # Placeholder for actual home action


# Function to display the value of the 'Side' entry field
def set_side_slit(slit_type):
    entered_value = side_entries[slit_type].get()
    print(
        f"{slit_type} Side Set to: {entered_value}"
    )  # Placeholder for actual set action


# Function to home the 'Side' slit
def home_side_slit(slit_type):
    print(f"{slit_type} Side Homed")  # Placeholder for actual home action


# Setting up the main window
root = tk.Tk()
root.title("Slits")

# Dictionaries to hold the entry widgets for each slit type
front_entries = {}
side_entries = {}


# Function to create a slit frame
def create_slit_frame(container, slit_type):
    frame = tk.LabelFrame(container, text=slit_type)
    frame.pack(padx=10, pady=10, fill="x")

    # Front Entry, Set and Home
    tk.Label(frame, text="Front:").grid(row=0, column=0)
    front_entry = tk.Entry(frame)
    front_entry.grid(row=0, column=1)
    front_entries[slit_type] = front_entry
    tk.Button(frame, text="Set", command=lambda: set_front_slit(slit_type)).grid(
        row=0, column=2
    )
    tk.Button(
        frame, text="Home Front", command=lambda: home_front_slit(slit_type)
    ).grid(row=1, column=0, columnspan=3, sticky="ew")

    # Side Entry, Set and Home
    tk.Label(frame, text="Side:").grid(row=2, column=0)
    side_entry = tk.Entry(frame)
    side_entry.grid(row=2, column=1)
    side_entries[slit_type] = side_entry
    tk.Button(frame, text="Set", command=lambda: set_side_slit(slit_type)).grid(
        row=2, column=2
    )
    tk.Button(frame, text="Home Side", command=lambda: home_side_slit(slit_type)).grid(
        row=3, column=0, columnspan=3, sticky="ew"
    )


# Create two slit frames
create_slit_frame(root, "Entrance Slit")
create_slit_frame(root, "Exit Slit")

# Run the main loop
root.mainloop()
