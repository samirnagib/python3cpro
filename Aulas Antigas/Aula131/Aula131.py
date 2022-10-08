f = open("demofile.txt", "r", encoding="UTF-8")
# print(f.read(7))
# print(f.readline())
# print(f.readline())

for x in f:
    print(x)

f.close()
