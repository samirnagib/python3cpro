import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

tk.Label(root, text="Label Classico").pack()
ttk.Label(root, text="Label Temático").pack()

tk.Button(root, text="Button Classico").pack()
ttk.Button(root, text="Button Temático").pack()

root.mainloop()
