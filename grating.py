import tkinter as tk
from tkinter import Listbox, END


# Функція для запису вибраної дифракційної решітки до файлу grating.conf
def set_grating():
    selected_grating = grating_list.get(grating_list.curselection())
    with open("grating.conf", "w") as file:
        file.write(selected_grating)
    print(f"Grating set to: {selected_grating}")  # Для перевірки; можна видалити


# Налаштування головного вікна
root = tk.Tk()
root.title("Grating")

# Створення списку для вибору дифракційної решітки
grating_list = Listbox(root, selectmode=tk.SINGLE, exportselection=False)
grating_items = [
    "Grating One",
    "Grating Two",
    "Grating Three",
    "Grating Four",
    "Grating Five",
    "Grating Six",
]
for item in grating_items:
    grating_list.insert(END, item)
grating_list.pack(side=tk.LEFT)

# Створення кнопки "Set"
set_button = tk.Button(root, text="Set Grating", command=set_grating)
set_button.pack(side=tk.RIGHT)

# Виконання головного циклу
root.mainloop()
