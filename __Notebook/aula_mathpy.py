import math
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

x = [5,200,3,2,150,98,24,11,10,7,9,26,34,25]

#print(min(x))
#print(max(x))


for item in x:
    print(item, "elevado ao quadrado é", '{:,.2f}'.format(math.pow(item,2)))
    
    
print(math.pi)