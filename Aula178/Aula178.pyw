import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Button Widget")
root.geometry("600x400+650+300")

def executar():
    root.quit()

btn1 = ttk.Button(
    root,
    text="Sair",
    command=executar
)
btn1.pack()

btn2 = ttk.Button(
    root,
    text="Sair Lambda",
    command=lambda: root.quit()
)
btn2.pack()

root.mainloop()
