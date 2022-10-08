import os
import shutil

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    print("Arquivo excluído.")
else:
    print("O arquivo não existe.")

if os.path.exists("Teste"):
    # os.rmdir("Teste")
    shutil.rmtree("Teste")
    print("Pasta excluída.")
else:
    print("A pasta não existe.")
