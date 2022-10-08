import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print("Tecla enter pressionada")

def log(event):
    print(event)

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

btn1 = ttk.Button(root, text="Executar")
btn1.bind("<Return>", return_pressed)
btn1.bind("<Return>", log, add="+")
btn1.focus()
btn1.pack(expand=True)

root.mainloop()
