import json

#jason -> dict
x = '{"nome":"Samir", "idade":42, "cidade":"Rio de Janeiro"}'
y = json.loads(x)

print(y)


#dict -> jason
a = {
    "nome": "Samir", 
    "idade": 42,
    "cidade": "Rio de Janeiro"}
b = json.dumps(a, indent=4)

print(b)