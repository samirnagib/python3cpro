import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

label1 = ttk.Label(
    root,
    text="Este é um label\nCurso Python Tkinter",
    background="yellow",
    foreground="red",
    padding=20,
    width=30,
    justify="left", #RIGHT LEFT RIGHT
    anchor=tk.E #N S E W NE NW SE SW CENTER 
)
label1.pack()

root.mainloop()
