import tkinter as tk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("600x400+500+200")

# Para garantir que uma janela esteja sempre no topo
root.attributes("-topmost", 1)

# Para mover uma janela para cima
# root.lift()

# Para mover uma janela para baixo
# root.lower()

root.mainloop()
