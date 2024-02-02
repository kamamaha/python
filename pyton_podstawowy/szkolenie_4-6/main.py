#Instrukcje warunkowe////////////////////////////////////////////////////
# Zadanie 1..........................................
import random

# dlugosc1 = int(input("Podaj pierwszą długość boku: "))
# dlugosc2 = int(input("Podaj drugą długość boku: "))
# dlugosc3 = int(input("Podaj trzecią długość boku: "))
#
# if dlugosc1**2 + dlugosc2**2 < dlugosc3**2:
#     print("Trójkąt nie jest prostokątny")
# elif dlugosc1**2 + dlugosc2**2 > dlugosc3**2:
#     print("Trójkąt nie jest prostokątny")
# else:
#     print("Trójkąt jest prostokątny")

# Zadanie 2.............................................

# podaj_liczbe = float(input("Podaj liczbę: "))
# if podaj_liczbe < 0:
#     print("Podana liczba jest ujemna")
# elif podaj_liczbe > 0:
#     print("Podana liczba jest dodatnia")
# else:
#     print("Podana liczba jest równa 0")

#Zadanie 3..........................................................

# podaj_liczbe1 = int(input("Podaj pierwszą liczbę: "))
# podaj_liczbe2 = int(input("Podaj drugą liczbę: "))
# podaj_liczbe3 = int(input("Podaj trzecią liczbę: "))
#
# zbior_liczb = [podaj_liczbe1, podaj_liczbe2, podaj_liczbe3]
# print(max(zbior_liczb))

#Zadanie 4............................................................
# JAK ZAKOŃCZYĆ DZIAŁANIE PO PIERWSZEJ WPISANEJ ZŁEJ WARTOŚCI?

# ENUMY
# FUKNCJE LOGICZNE
# import sys
# podaj_wariant1 = input("kamień, papier, nożyce?: ")
#
# if podaj_wariant1 in ["kamień", "papier", "nożyce"]:
#     podaj_wariant2 = input("kamień, papier, nożyce?: ")
#     if podaj_wariant2 in ["kamień", "papier", "nożyce"]:
#         print(podaj_wariant1)
#         print(podaj_wariant2)
#         if podaj_wariant1 == podaj_wariant2:
#             print("Remis")
#         elif podaj_wariant1 == "kamień" and podaj_wariant2 == "nożyce" or  podaj_wariant1 == "kamień" and podaj_wariant2 == "papier" or podaj_wariant1 == "nożyce" and podaj_wariant2 == "papier" or podaj_wariant1 == "nożyce" and podaj_wariant2 == "kamień":
#             print("Wygrał zawodnik nr 1")
#         else:
#             print("Wygrał zawodnik 2")
# else:
#     sys.exit()

# while True:
#     podaj_wariant2 = input("kamień, papier, nożyce?: ")
#     if (podaj_wariant1 == "kamień" or podaj_wariant1 == "papier" or podaj_wariant1 == "nożyce") and (podaj_wariant2 == "kamień" or podaj_wariant2 ==  "papier" or podaj_wariant2 ==  "nożyce"):
#         if podaj_wariant1 == "kamień" and podaj_wariant2 == "nożyce":
#             print("Wygrał zawodnik nr 1")
#         elif podaj_wariant1 == "kamień" and podaj_wariant2 == "papier":
#             print("Wygrał zawodnik nr 2")
#         elif podaj_wariant2 == "kamień" and podaj_wariant1 == "nożyce":
#             print("Wygrał zawodnik nr 2")
#         elif podaj_wariant2 == "kamień" and podaj_wariant1 == "papier":
#             print("Wygrał zawodnik nr 1")
#
#         elif podaj_wariant1 == "nożyce" and podaj_wariant2 == "papier":
#             print("Wygrał zawodnik nr 1")
#         elif podaj_wariant1 == "nożyce" and podaj_wariant2 == "kamień":
#             print("Wygrał zawodnik nr 2")
#         elif podaj_wariant2 == "nożyce" and podaj_wariant1 == "papier":
#             print("Wygrał zawodnik nr 2")
#         elif podaj_wariant2 == "nożyce" and podaj_wariant1 == "kamień":
#             print("Wygrał zawodnik nr 1")
#
#         elif podaj_wariant1 == "papier" and podaj_wariant2 == "nożyce":
#             print("Wygrał zawodnik nr 2")
#         elif podaj_wariant1 == "papier" and podaj_wariant2 == "kamień":
#             print("Wygrał zawodnik nr 1")
#         elif podaj_wariant2 == "papier" and podaj_wariant1 == "nożyce":
#             print("Wygrał zawodnik nr 1")
#         elif podaj_wariant2 == "papier" and podaj_wariant1 == "kamień":
#             print("Wygrał zawodnik nr 2")
#
#         elif podaj_wariant1 == podaj_wariant2:
#             print("Remis")
#
#     else:
#         print("Błędne dane")

#Zadanie 5.........................................................................

# podaj_liczbe1 = float(input("Podaj pierwszą liczbę: "))
# podaj_liczbe2 = float(input("Podaj drugą liczbę: "))
#
# if podaj_liczbe1 >= 0 or podaj_liczbe2 >= 0:
#     print("Co najmniej jedna liczba jest liczbą parzystą")
# else:
#     print("Podane liczby są liczbami nieparzystymi")

# Zadanie 6.....................................................................
#JAK PRZERYWAĆ PROGRAM PO PODANIU ZŁYCH WARTOSCI / Źle przypisuje wartosci jak?

# import random
# uzytkownik = 0
# komputer = 0
# zaklad = input("Co wybierasz?: ")
# if zaklad == "o" or zaklad == "r":
#     if zaklad == "o":
#         zaklad = 0
#         print("Wybrałeś orła")
#     elif zaklad == "r":
#         zaklad = 1
#         print("Wybrałeś reszkę")
# else:
#     print("Błędne dane")
#
# rzut = random.randint(0,1)
# print("""
# 3
# 2
# 1...""")
# print(("Wynik rzutu to: ", rzut))
#
# if zaklad == rzut:
#     uzytkownik += 1
# else:
#     komputer += 1
#
# print("Użytkownik punkty: ", uzytkownik)
# print("Komputer punkty: ", komputer)

# PĘTLE /////////////////////

# Zadanie 1...........................................................

# liczba = int(input("Podaj liczbę: "))

# for i in range(0, liczba + 1):
#     print(i)

# stan_poczatkowy = 0
# while stan_poczatkowy <= liczba:
#     print(stan_poczatkowy)
#     stan_poczatkowy += 1

#Zadanie 2...........................................................

# for i in range(100, 49, -1):
#     print(i)

# i = 100
# while i != 49:
#     print(i)
#     i -= 1

# Zadanie 3..............................................................

# for i in range(0, 101, 5):
#     print(i)

# a = 1
# b = 102
# while a != b:
#     print(a - 1)
#     a += 5

#Zadanie 4....................................................................

# nie wiem

# Zadanie 5....................................................................

# nie wiem

# Zadanie 7

# for i in range(1):
#     print("*" * 10)

# ilosc_wierszy = 4
# ilosc_gwiazdek = 1
#
# for i in range(ilosc_wierszy):
#     for i in range(ilosc_gwiazdek):
#         print("*", end=" ")
#     print()
#     ilosc_gwiazdek += 1

# ilosc_wierszy = 3
# for i in range(ilosc_wierszy):
#     print("*" * 3)

#Zadanie 9.....................................................................


# ilosc_astronautow = int(input("Podaj ilość astronautów: "))
# wysokosc = int(input("Na jakiej wysokości znajduje się rakieta?: "))

# while True:
#     try:
#         poczatkowy_poz_paliwa = int(input("Podaj początkowy poziom paliwa: "))
#     except ValueError:
#         print("Zła wartość")
#     if poczatkowy_poz_paliwa < 5000 and poczatkowy_poz_paliwa > 30000:
#         print(("Niewystarczający poziom paliwa"))
#         continue
#     else:
#         break
#     if poczatkowy_poz_paliwa >= 5000 and poczatkowy_poz_paliwa <= 30000:
#         print("Twój poziom paliwa jest odpowiedni")
#     else:
#         print("Twój poziom paliwa nie jest odpowiedni")

# Zadania Szkolenie 4 – 6

# Zadanie 1

# for i in range(10):
#     print("Elo")

# Zadanie 2

# podaj_liczbe = int(input("Podaj liczbę: "))
# suma = 0
#
# for i in range(1, podaj_liczbe + 1):
#     suma += i
# print(suma)

# Zadanie 3

# n = int(input("Ile chcesz wprowadzić liczb?: "))
# liczby = []
# for i in range(n):
#     a = int(input("Podaj liczbe nr {}: ".format(int(i) + 1)))
#     if a % 2 == 0:
#         liczby.append(a)
# print(liczby)

# Zadanie 4

# podaj_liczbe = int(input("Podaj liczbę: "))
#
# while True:
#     if podaj_liczbe == 1:
#         print("poniedziałek")
#     elif podaj_liczbe == 2:
#         print("wtorek")
#     elif podaj_liczbe == 3:
#         print("środa")
#     elif podaj_liczbe == 4:
#         print("czwartek")
#     elif podaj_liczbe == 5:
#         print("piątek")
#     elif podaj_liczbe == 6:
#         print("sobota")
#     elif podaj_liczbe == 7:
#         print("niedziela")
#     else:
#         print("nie ma takiego dnia")
#     break

# Zadanie 5

# d = (1, [2, 4], "tekst", 3 +5j)
#
# print(d[3])
# print(d[0:2])
# print("abc" in d)

#Zadanie 6

# a = [3, 1, 5, 7, 9, 2, 6]
# print(a[3])
# print(a[1:4])
# print(a[3:])
# print(a[-3:])
# print(a[:3])
# print(a[3:-1])
# print(a[::2])
# print(a[5:2:-1])
# print(sum(a))
# print(8 in a)
# print(4 not in a)

# Zadanie 7

# podaj_liczbe = int(input("Podaj liczbe: "))
# if podaj_liczbe < 0:
#     wart_bezwzglenda = podaj_liczbe * (-1)
#     print(wart_bezwzglenda)
# else:
#     print(podaj_liczbe)

#Zadanie 9

# print(True and False)
# print(True and True)
# print(False or False)
# print(False or True)

# Zadanie 10


# Zadanie 11

# for i in range(6):
#     print("*" * 6)

# for i in range(0, 1):
#     print("*" * 5)
#     for j in range(3):
#         print("*   *")
# print("*" *5)

# for i in range(1):
#     for j in range(1):
#         print("*".center(20))
#     for k in range(1):
#         print("***" .center(20))
#     for l in range(1):
#         print("*****".center(20))
#     for m in range(1):
#         print("*******" .center(20))
#     for m in range(1):
#         print("*********".center(20))

# Zadanie 12
# a = ["a", "b", "c", "d", "e"]
# word = [i.upper() for i in a]
# word.reverse()
# print(word)

#Zadanie 13

# podaj_slowo = [input("Podaj klucz: ")]
# podaj_definicje = [input("Podaj definicje: ")]
#
# a = podaj_slowo + podaj_definicje
# print(a)
#
# slownik = dict(zip(podaj_slowo, podaj_definicje))
# print(slownik)
#
# if "Kama" in slownik:
#     print(" istnieje w słowniku")
# else:
#     print("Podany klucz nie istnieje w słowniku")
#
# if "Kama" in slownik:
#   print(slownik.pop("Kama"))
#   print(slownik)
# else:
#   print("Nie ma takiego klucza w słowniku")

# Zadanie 15

# slownik = {"000000000001": ["niebieskie", "Robert", "Grządko", "11"],
#            "000000000002": ["brązowe", "Kamil", "Nowak", "30"],
#            "000000000003": ["zielone", "Paweł", "Kowalski", "35"],
#            "000000000004": ["czarne", "Dawid", "Bobo", "15"],
#            "000000000005": ["fioletowe", "Andrzej", "Musioł", "56"],
#            }
# print(slownik)

# import random
#
# a = int(input("Podaj dolny przedział: "))
# b = int(input("Podaj górny przedział: "))
#
# wylosowana_liczba = random.randint(a, b)
# print(wylosowana_liczba)
#
# c = int(input("Podaj liczbę: "))
#
# while c != wylosowana_liczba:
#     if wylosowana_liczba > c:
#         print("Podałeś za małą liczbę")
#     elif wylosowana_liczba < c:
#         print("Podałeś za dużą liczbę")
#     c = int(input("Podaj liczbę: "))
# print("Podałeś dobra liczbę")