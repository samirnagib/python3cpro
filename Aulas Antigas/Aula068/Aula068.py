def myFunction():
    print("Ola de dentro da função.")

def cumprimenta(nome):
    print("Ola ", nome)

def multiplica(x):
    return x * 5
    
myFunction()
cumprimenta("Gabriel")
cumprimenta("Danny")

result = multiplica(2)
print(result)

print(multiplica(5))

for x in range(1024):
    print(multiplica(x))