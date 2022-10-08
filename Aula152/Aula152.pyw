import tkinter as tk

root = tk.Tk()

root.title("Minha Aplicação GUI")

titulo = root.title()

lbl = tk.Label(root, text=titulo)
lbl.pack()

root.mainloop()
