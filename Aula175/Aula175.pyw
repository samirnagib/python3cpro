import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

label1 = ttk.Label(
    root,
    text="Label Temático",
    font="Arial 24",
    borderwidth=10,
    relief="groove" #"groove", "ridge", "sunken", "raised", flat
)
label1.pack()

label2 = tk.Label(
    root,
    text="Label Padrão",
    font="Arial 24",
    borderwidth=10, #bd
    relief="groove"
)
label2.pack()

root.mainloop()
