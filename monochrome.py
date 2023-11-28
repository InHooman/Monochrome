import tkinter as tk
import subprocess
from tkinter import messagebox

# Функція для запуску скрипта, який відповідає натиснутій кнопці
def launch_script(script_name):
    subprocess.run(["python", f"{script_name}.py"], check=True)

# Функція для відображення інформації про програму
def show_about():
    messagebox.showinfo("About", "Monochrome.py\nVersion 0.4")

# Налаштування головного вікна
root = tk.Tk()
root.title("Monochrome")
root.geometry("1280x720")

# Визначення назв кнопок для двох рядів
button_names_row1 = ["Operation", "Grating", "Slits"]
button_names_row2 = ["Defaults"]

# Створення фрейму для розміщення кнопок по центру
button_frame = tk.Frame(root)
button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Створення та розміщення кнопок для першого ряду в середині фрейму
for i, name in enumerate(button_names_row1):
    button = tk.Button(
        button_frame,
        text=name,
        command=lambda n=name: launch_script(n),
        height=2,
        width=20,
    )
    button.grid(row=0, column=i, padx=5, pady=2)

# Створення та розміщення кнопок для другого ряду в середині фрейму
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(len(button_names_row1), weight=1)
for i, name in enumerate(button_names_row2):
    button = tk.Button(
        button_frame,
        text=name,
        command=lambda n=name: launch_script(n),
        height=2,
        width=20,
    )
    button.grid(row=1, column=len(button_names_row1)//2, padx=5, pady=5)

# Створення кнопки "Про програму" в нижньому правому куті
about_button = tk.Button(root, text="About", command=show_about)
about_button.place(relx=1.0, rely=1.0, anchor=tk.SE)

# Виконання головного циклу
root.mainloop()
