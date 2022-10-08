import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

foto = tk.PhotoImage(file="imagens/Python.png")

label1 = ttk.Label(
    root,
    image=foto,
    text="Logo Python",
    font="Arial 20",
    compound="top" #'top','bottom','left','right','none','text','image'
)
label1.pack()

root.mainloop()
