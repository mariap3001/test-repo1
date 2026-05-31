# bool
# typ prosty / prymitywny

prawda = True
falsz = False

a = "ABC"

sprawdz1 = a.isnumeric()
sprawdz2 = a.islower()

print(sprawdz1)

X = 7 > 4


a = 15

if a >= 10:
    print("zgadza się")
    print("kolejna operacja")
    print("jeszcze jedna")
    # blok kodów if
    #odpali się jeśli warunek jest spełniony

else:
    print("liczba jest za mała")










koszyk = 198.00
kod = "ABC2026"
kraj = "PL"

if koszyk > 150 or kod == "ABC2026":
    print("uzyskano rabat")
else:
    print("brak rabatu")


login = "admin123"
dzien = "piatek"
aktualizacja = True


if login == "admin123" and (dzien == "sobota" or aktualizacja):
    print("można przeprowadzić update")


user_role = "admin"
is_logged = True

if user_role == "admin" and is_logged:
    print("Witaj w panelu admina")
elif is_logged and user_role == "moderator":
    print("Witaj w panelu moderstora")
elif is_logged and user_role == "user":
    print("Witaj w panelu użytkownika")
else:
    print("Błąd logowania")


user_country = "Polska"
if user_country in ["Polska", "Niemcy", "Czechy"]:
    print("Dostawa możliwa")
else:
    print("Dostawa towaru niemożliwa")


from datetime import datetime
aktualna_godzina = datetime.now().hour

if 6 <= aktualna_godzina < 12:
    print("Good Morning")
elif 12 <= aktualna_godzina < 18:
    print("Good Afternoon")
else:
    print("Good Evening")



    # Do prawdy: -99...99, ".."
    # Do fałszu: 0,"", None

    konwersja = bool(None)
    print(konwersja)


#logowanie

email = "jan@gmail.com"
if email:
    inicjaly = email[0].upper()
    print(inicjaly)