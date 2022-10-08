import platform

for item in dir(platform):
    print(item)
    
print(platform.java_ver())
print(platform.processor())
print(platform.platform())
print(platform.system())
print(platform.machine())


