import tkinter as tk
from tkinter import scrolledtext


def load_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."


def display_file_content():
    # Load the content of the file
    file_content = load_file_content("default.conf")

    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Display File Content")

    # Create a scrolled text area widget
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Insert the file content to the text area
    text_area.insert(tk.INSERT, file_content)

    # Make the text area read-only
    text_area.config(state=tk.DISABLED)

    # Start the Tkinter event loop
    window.mainloop()


# Call the function to display the file content
display_file_content()
