import tkinter as tk

root = tk.Tk()
root.title("Minha Aplicação GUI")

window_width = 600
window_height = 400

# Obter as dimensões da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Encontrar o ponto central
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

#  Definir a posição da janela no centro da tela
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

root.mainloop()
