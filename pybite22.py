# coding: utf-8

print("type(1):", type(1))

# w etykieta opakowujemy typ integer
etykieta = type(1)
print("type(etykieta):", type(etykieta))
print("etykieta:", etykieta)

print("int(3.14):", int(3.14))
print("etykieta(3.14):", etykieta(3.14))


def f(x, y):
    return x + y

print("type(f):", type(f))

# mamy nową etykietę dla funkcji f
g = f

print("g(1, 2):", g(1, 2))
print("g:", g)
print("type(g):", type(g))


def m(x, y):
    return x - y

def operacja(operator, x, y):
    return operator(x, y)

print("operacja f:", operacja(f, 1, 2))
print("operacja m:", operacja(m, 1, 2))

# dekorator opakowuje funkcję w dodatkowe czary-mary ;)

def operacja2(operator, x, y):
    return operator(x, y) + 5

def dek(f, *args, **kwargs):
    return f(*args, **kwargs)

# stara notacja dekoratora
# nazwa dekoratora
#@dekorator
#def funkcja(x, y):
#    return x + y

# opakowanie funkcji w dekorator
#funkcja = dekorator(funkcja)

class Klasa:
    # metoda klasy; cls przekazuje klasę, a nie obiekt
    @classmethod
    def policz_instancje(cls):
        pass

    # metoda statyczna, nie przekazujemy obiektu self jako argumentu
    @staticmethod
    def powiedz(komunikat):
        print(komunikat)

    # potem odwołujemy się do takiej właściwości obj.ile - nie jak do funkcji
    # setter + getter ~= property
    # można dać przypisanie obj.ile = 6, ale trzeba pamiętać o dodatkowym argumencie w definicji def ile(self, val)
    @property
    def ile(self):
        return self.liczba

    # możemy się odwoływać do składowych klasy za pomocją notacji tablicy asocjacyjnej obj["nazwa"]; można też uzyskać atrybuty __getattr__
    def __getitem__(self, key):
        #return sth
        pass
