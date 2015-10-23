# coding: utf-8

import sys

# faktoriał - silnia

def silnia_rek(n):
    if n == 0:
        return 1
    else:
        return n * silnia_rek(n - 1)

# ciakawa składnia, podobnie robiłem z for do generowania elementów listy lub krotki
# return 1 if n == 0 else n * silinia_rek(n-1)

def silnia_iter(n):
    wynik = 1
    while n >= 1:
        # wynik nie jest lokalny, bo już wcześniej go zainicjowaliśmy
        # w strukturach iteracyjnych też możemy mieć zmienne lokalne - tak jak w funkcjach
        wynik = wynik * n
        n -= 1
    return wynik

#for i in range(0, 11):
#    print("silnia rek %d" % i, silnia_rek(i))
#    print("silnia iter %d" % i, silnia_iter(i))

# jest ograniczenie na ilość wywołań rekurencyjnych w py - 1000
# jest to zależne od implementacji

print("default limit:", sys.getrecursionlimit())
print(len(str(silnia_rek(600))))
# maximum
print(len(str(silnia_rek(997))))

# z tym trzeba uważać
sys.setrecursionlimit(1500)
print("new limit:", sys.getrecursionlimit())
print(len(str(silnia_rek(1450))))

# dla iteracyjnej metody ogranicza nas pamięć
print(len(str(silnia_iter(1500))))

# py potrafi zrobić obliczenie, zapisać je i dalej na nim operować, używając swoich standardowych typów
