import tkinter as tk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

# Apresentar maximizada
# root.state("zoomed")

# Apresentar minimizada
# root.state("iconic")

# Apresentar normal
root.state("normal")

# print(root.state())
# root.title(root.state())

root.mainloop()
