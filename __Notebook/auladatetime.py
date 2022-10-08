import datetime
import locale

lastday = datetime.timedelta(days=1)
x = datetime.date.today()-lastday

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
print(x.strftime("%A, %d/%m/%Y %H:%M:%S"))
