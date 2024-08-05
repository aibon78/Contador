import tkinter as tk
from tkinter import messagebox
import os

FILENAME = "death_counter.txt"

def load_counter():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return int(file.read())
            except ValueError:
                return 0
    return 0

def save_counter():
    with open(FILENAME, "w") as file:
        file.write(str(counter))

def increase_counter():
    global counter
    counter += 1
    label_counter.config(text=str(counter))
    save_counter()

def reset_counter():
    global counter
    response = messagebox.askyesno("Reset the counter", "Are you sure you want to reset the counter?")
    if response:
        counter = 0
        label_counter.config(text=str(counter))
        save_counter()

root = tk.Tk()
root.title("Death Counter - Sekiro")

# Configuração da janela principal
root.configure(bg="#696969")

counter = load_counter()

# Estilização do label_counter
label_counter = tk.Label(root, text=str(counter), font=("Helvetica", 24), bg="#696969", fg="#B22222")
label_counter.pack(pady=20)

# Estilização do botão de aumento
button_increase = tk.Button(root, text="Increase", command=increase_counter, font=("Helvetica", 14),
                            bg="#007bff", fg="white", activebackground="#0056b3", activeforeground="white",
                            bd=0, padx=20, pady=10)
button_increase.pack(pady=10)

# Estilização do botão de reset
button_reset = tk.Button(root, text="Reset", command=reset_counter, font=("Helvetica", 14),
                         bg="#007bff", fg="white", activebackground="#0056b3", activeforeground="white",
                         bd=0, padx=20, pady=10)
button_reset.pack(pady=10)

root.mainloop()
