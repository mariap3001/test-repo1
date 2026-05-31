import datetime

x = datetime.datetime.now()
print(x)

from datetime import datetime

x = datetime.now()
rok = x.year
miesiac = x.month
dzien = x.day
print(f"{dzien}/{miesiac}/{rok}")

data = x.strftime("%d/%m/%y, %H:%M:%S")
print(data)


zalogowany = True
wiadomosc = "Witaj w apce" if zalogowany else "Musisz sie zalogować"

print(wiadomosc)



