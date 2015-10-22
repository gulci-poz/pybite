# coding: utf-8

# faktoriał - silnia

def silnia_rek(n):
    if n == 0:
        return 1;
    else:
        return n * silnia_rek(n - 1)



def silnia_iter(n):
    wynik = 1
    while n >= 1:
        # wynik nie jest lokalny, bo już wcześniej go zainicjowaliśmy
        # w strukturach iteracyjnych też możemy mieć zmienne lokalne - tak jak w funkcjach
        wynik = wynik * n
        n -= 1
    return wynik

for i in range(0, 11):
    print("silnia rek %d" % i, silnia_rek(i))
    print("silnia iter %d" % i, silnia_iter(i))

# 3 - 59 min
