import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Widget")
root.geometry("600x400+650+300")

label1 = ttk.Label(
    root,
    text="Este é um label",
    font=("Verdana", 36, "bold", "italic") # font="Times 24 bold italic"
)
label1.pack()

root.mainloop()
