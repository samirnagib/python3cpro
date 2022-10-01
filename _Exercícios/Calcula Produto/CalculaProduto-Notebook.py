import os
import platform

def limpaTela():
    so = platform.system()
    if "windows" in so.lower():
        os.system("cls") or None
    else:
        os.system("clear") or None

limpaTela()
print("Ok")