import math


def prime(*liczby):
    for liczba in liczby:
        czy_pierwsza = True
        if liczba < 2:
            czy_pierwsza = False
        for i in range(2, int(math.sqrt(liczba)) + 1):
            if liczba%i == 0:
                czy_pierwsza = False
        if czy_pierwsza:
            print(str(liczba) + " is prime number")
        else:
            print(str(liczba) + " is not prime")


prime(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
