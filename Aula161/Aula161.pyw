import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

# Usando argumentos de palavra-chave ao criar o widget
ttk.Label(root, text="Ola Mundo!").pack()

# Usando um índice de dicionário após a criação do widget
lbl1 = ttk.Label(root)
lbl1["text"] = "Outro Ola Mundo!"
lbl1.pack()

# Usando o método config() com atributos de palavra-chave
lbl2 = ttk.Label(root)
lbl2.config(text="Mais um Ola Mundo!")
lbl2.pack()

root.mainloop()
