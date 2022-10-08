from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# usando a chave gerada
fernet = Fernet(key)

# abrindo o arquivo original para criptografar
with open('d:\\_Cursos\\python3cpro\\__Notebook\\original.txt', 'rb') as file:
    original = file.read()

# criptografar o arquivo
encrypted = fernet.encrypt(original)

# abrir o arquivo no modo de gravação e
# gravar os dados criptografados
with open('d:\\_Cursos\\python3cpro\\__Notebook\\encriptado.txt', 'w+b') as encrypted_file:
    encrypted_file.write(encrypted)
    
# abrindo o arquivo criptografado
with open('d:\\_Cursos\\python3cpro\\__Notebook\\encriptado.txt', 'rb') as enc_file:
    encrypted = enc_file.read()

# descriptografando o arquivo
decrypted = fernet.decrypt(encrypted)

# abrindo o arquivo no modo de gravação e
# gravando os dados descriptografados
with open('d:\\_Cursos\\python3cpro\\__Notebook\\novooriginal.txt', 'wb') as dec_file:
    dec_file.write(decrypted)