from cryptography.fernet import Fernet
# geração de chave
key = Fernet.generate_key()

# string a chave em um arquivo
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)