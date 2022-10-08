import tkinter as tk

root = tk.Tk()
root.title("Minha Aplicação GUI")
root.geometry("1024x768+500+200")

# janela.metodo(largura, altura)
root.resizable(True, True)
root.minsize(300, 200)
root.maxsize(800, 600)

root.mainloop()
