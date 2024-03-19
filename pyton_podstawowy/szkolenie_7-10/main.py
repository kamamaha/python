# Zadanie 1 #######################################################################
import random


# nums = [4, 6, 8, 24, 12, 2]
# def max_index():
#    a = [index for index, value in enumerate(nums) if value == max(nums)]
#    print(a)
# max_index()

# Zadanie 3 #######################################################################

# def fizz_buzz(a):
#     if a % 3 == 0:
#         print("Frizz")
#     elif a % 5 == 0:
#         print("Buzz")
#     elif a % 3 == 0 and a % 5 == 0:
#         print("FrizzBuzz")
#     else:
#         print(a)
# fizz_buzz(13)

# Zadanie 4 #######################################################################

# def multiply(*args):
#     number = 1
#     for a in args:
#         number *= a
#     return number
# print(multiply(2, 10, 10))

# Zadanie 5 #######################################################################
# NIE WIEM
# Zadanie 6 #######################################################################

# def select_list(list):
#     for i in list:
#         if i >= 10:
#             print(i)

# a = [1,2,4,5,6,7,8,9,11,12]
# select_list(a)

# Zadanie 6 #######################################################################

# def select_numbers(numbers):
#     for number in numbers:
#         if number >= 10:
#             print(number)

# numbers = [2, 5, 7, 8, 10, 15, 34, 76, 13, 64]
# select_numbers(numbers)

# Zadanie 8 #######################################################################


# KLASY ...........................................................................
# Zadanie 1 #######################################################################

# class Student():
#     """informations about student"""
#     def __init__(self, name, lastname, age, degree):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.degree = degree
#     def print_info(self):
#         print("Student nazywa się " + self.name.title() + " " + self.lastname.title() + " ma lat " + str(self.age) + " i studiuje " + self.degree.title())
#
# student = Student("Paweł", "Nowak", 13, "informatyka")
# student.print_info()

# Zadanie 2 #######################################################################

# class Car():
#     def __init__(self, max_speed, odometr):
#         """Info about car"""
#         self.max_speed = max_speed
#         self.odometr = odometr
#     def describe_car_info(self):
#         print("Samochód ma przejechane: " + str(self.odometr) + " km oraz jego max prędkość to: " + str(self.max_speed))
#     def reading_odometr(self):
#         """Show info about odometr"""
#         print("Przebieg danego samochodu wynosi: " + str(self.odometr))
#     def update_odometr(self, km):
#         self.odometr = km
#
# new_car = Car(250.5, 0)
# print(new_car.describe_car_info())
# new_car.update_odometr(500)
# new_car.reading_odometr()

# Zadanie 3 #######################################################################

# class Square():
#     def __init__(self, length, width):
#         """"Określanie długości i szerokości prostokąta"""
#         self.length = length
#         self.width = width
#     def info_square(self):
#         print("Długość prostokąta to: " + str(self.length) + " a szerkość to: " + str(self.width))
#     def area_of_a_rectangle(self):
#         result = self.length * self.width
#         return print("Pole prostokąta to: " + str(result))
#     def circumference_of_a_rectangle(self):
#         result2 = 2 * (self.length) + 2 * (self.width)
#         return print("Obwód prostokąta to: " + str(result2))
#
# new_square = Square(10, 20)
# new_square.info_square()
# new_square.area_of_a_rectangle()
# new_square.circumference_of_a_rectangle()

# Zadanie 4 #######################################################################

# class BankAccount():
#     def __init__(self, account_number, owner, state_account):
#         self.account_number = account_number
#         self.owner = owner
#         self.state_account = state_account
#
#     def deposit(self):
#         """"Kwota ile będzie wpłacane na konto"""
#         deposit_amount = int(input("Ile chcesz wpłacić gotówki: "))
#         commission = int(deposit_amount/100) * 2
#
#         new_deposit_amount = deposit_amount - commission
#         self.state_account = new_deposit_amount + self.state_account
#         return self.state_account
#
#     def withdraw(self):
#         withdraw_amount = int(input("Ile chcesz wypłacić gotówki: "))
#
#         if withdraw_amount > self.state_account:
#             print("Nie możesz wypłacić tej kwoty, nie masz wystarczająco gotówki na koncie!")
#         else:
#             self.state_account = self.state_account - withdraw_amount
#             return self.state_account
#
#     def change_ownership(self):
#         new_owner = input("Imię nowego właściciela: ")
#         self.owner = new_owner
#         print("Nowy właściel to: " + self.owner.title())
#     def display(self):
#         print("Twoje konto ma obecnie: " + str(self.state_account) + " oraz zmieniono nazwę nowego właściela na: " + str(self.owner))
#
# new_bank_account = BankAccount(1234556778, "Kamila Grządko", 100)
# print(new_bank_account.deposit())
# print(new_bank_account.withdraw())
# new_bank_account.change_ownership()
# new_bank_account.display()

# Zadanie 5 #######################################################################

# class Card:
#     def __init__(self, value, figure):
#         self.value = value
#         self.figure = figure
#
#     def show_card(self):
#         return self.value, self.figure
#
#
# class Deck:
#     cards = []
#     def __init__(self):
#         values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]
#         figures = ["heart", "diamond", "club", "spade"]
#         self.cards = []
#         for value in values:
#             for figure in figures:
#                 self.cards.append(Card(value, figure))
#
#     def show_deck(self):
#         return self.cards
#     def all_deck(self):
#         for i in range(len(self.cards)):
#             print(f"{i+1}{self.cards[i].show_card()}")
#     def draw_card(self):
#         import random
#         card = random.choice(self.cards)
#         self.cards.remove(card)
#         return card
#     def __str__(self):
#         return "hello"
#     def __add__(self, other):
#         return self.cards + other.cards
#
# deck = Deck()
# print(Deck())
# print(len(Deck() + Deck()))
# print(deck.cards.__len__() == len(deck.cards))
# print(deck.all_deck())


# DZIEDZICZENIE ...........................................................................

# ZADANIE 1 ######################################################

# class Shape:
#     def __init__(self, width, length = 0):
#         self.width = width
#         self.length = length
#     def area(self):
#         area = self.width * self.length
#         return area
#
# class Square(Shape):
#     def __init__(self, width, length):
#         super().__init__(width, length)
#
# figure = Square(4, 10)
# print(figure.area())


# ZADANIE 2 ######################################################

class Zajezdnia:
    pass

class Pojazd:
    def __init__(self, max_szybkosc: float, numer_pojazdu: int, zajezdnia: Zajezdnia = None):
        self.max_szybkosc = max_szybkosc
        self.numer_pojazdu = numer_pojazdu
        self.zajezdnia = zajezdnia

class Tramwaj(Pojazd):
    def __init__(self, wagony: int) -> None:
        super().__init__(111, 12)
        self.wagony = wagony

    def ile_wagonow(self):
        lista_wagonow = []
        while True:
            wagon = input("Ile wagonów ma tramwaj: ")
            if wagon == "": break
            lista_wagonow.append(wagon)
        return lista_wagonow
    def __str__(self):
        return "Dany tramwaj ma nr " + str(self.numer_pojazdu) + " jeździ z max. szybkością " + str(self.max_szybkosc) + " km/h i posiada " + str(self.wagony) + " liczbę wagonów."

class ZajezdniaTramwajowa(Pojazd, Tramwaj):
    def __int__(self):



class ZajezdniaAutobusowa(Zajezdnia):

    # def __init__(self, zuzycie_paliwa: float, suma_msc_zuzycia_paliwa: float):
    #     self.zuzycie_paliwa = zuzycie_paliwa
    #     self.suma_msc_zuzycia_paliwa = suma_msc_zuzycia_paliwa
    #
    # def msc_zuzycie_paliwa(self):
    #     suma_msc_zuzycia_paliwa = 30 * self.zuzycie_paliwa
    #     return suma_msc_zuzycia_paliwa
    #
    # def __str__(self):
    #     return "Atobusy zużywają " + str(self.suma_msc_zuzycia_paliwa)
    pass
# class Autobus(Pojazd):
#     def __init__(self, zajezdnia: ZajezdniaAutobusowa, max_szybkosc: float, numer_pojazdu: int, ile_paliwa: float) -> None:
#         super().__init__(max_szybkosc, numer_pojazdu)
#         self.ile_paliwa = ile_paliwa
#
#     def __str__(self):
#         return "Dany autobus ma nr " + str(self.numer_pojazdu) + " jeździ z max. szybkością " + str(self.max_szybkosc) + " km/h i zużywa " + str(self.ile_paliwa) + " litrów paliwa na godzinę jazdy."


if __name__ == "__main__":
    tramwaj1 = Tramwaj(3)
    tramwaj1.ile_wagonow()
    print(tramwaj1.ile_wagonow())
    print(tramwaj1)
