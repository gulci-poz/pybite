# coding: utf-8

def nth(n):
    return n

# własność name istnieje dla każdej funkcji
print(nth.__name__)

def opakowator(funkcja, *args, **kwargs):
    def opakowanie(*inargs, **inkwargs):
        print("Wykonuję", funkcja.__name__)
        wynik = funkcja(*inargs, **inkwargs)

        return wynik

    return opakowanie

nth = opakowator(nth)

nth(32)
