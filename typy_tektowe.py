imie = "jan"
nazwisko = "kowalski"
miasto = "lodz"

wynik = "to jest" + imie + " " + nazwisko + ". Jego miejsce urodzenia to " + miasto

print(wynik)



result = "to jest krótkie zdanie na temat jana"

nowy_wynik = result.replace(" ", "-")

print(nowy_wynik)







from datetime import datetime
month = datetime.now().month

miesiac = None
match(month):
    case 1:
        miesiac = "Styczeń"
    case 5:
        miesiac = "Maj"
    case 12:
        miesiac = "Grudzień"
    case _:
        miesiac = "Brak"

print(miesiac)


#TRY...EXCEPT
#WYJĄTKI


x = input("Podaj liczbę: ")

#ktoś może: dzielić przez 0, brak liczby, nic nie podać
try:
    dzialanie = 100 / float(x)
    print(dzialanie)
except ZeroDivisionError as e:
    print("Nie możesz dzielić przez 0!")
    print(e)
except ValueError as e:
    print("Musisz podać liczbę!")
    print(e)
Except Exception 