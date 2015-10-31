# coding: utf-8

def funkcja(n):
    return n + 1

def inna_f(n):
    return n - 7

# funkcja jest obiektem
print(funkcja)

print("funkcja:", funkcja(2))
print("inna_f:", inna_f(2))

# można przekazać funkcję do funkcji jako parametr
def trzecia(f, n):
    return f(n) + 3

print("trzecia, funkcja:", trzecia(funkcja, 3))
print("trzecia, inna_f:", trzecia(inna_f, 3))

def opakowanie():
    def nowa():
        return 42
    return nowa

# opakowanie zwraca funkcję: nowa
testowa = opakowanie()
print(testowa)
# możemy ją wykonać
print("testowa:", testowa())

# dekorator to funkcja, która przyjmuje jako parametr funkcję (ale nie koniecznie, może to być dowolny parametr; mogą być dodatkowe parametry, również w postaci *args_outer i **kwargs_outer - można je potem wykorzystać w opakowanej funkcji), opakowuje ją i zwraca nową funkcję, która korzysta z tej przekazanej do dekoratora

def dekorator(fun):
    print("jestem dekoratorem")

    # opakowanie() powinna przyjmować te same parametry, co opakowywana funkcja; lub *args i **kwargs - będziemy je rozpakowywali

    def opakowanie(*args, **kwargs):
        print("jestem funkcją wewnętrzną")
        wynik = fun(*args, **kwargs)
        print("po wykonaniu opakowanej funkcji")

        return wynik

    return opakowanie

# inna (stara) notacja; musimy mieć wcześniej zdefiniowaną funkcję dekoratora
#@dekorator
# tutaj możemy podać dodatkowe parametry do dekoratora
#@dekorator(dodatkowy_parametr)
def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)

# dostajemy funkcję opakowanie, która wzbogaca (opakowuje) silnię
# przy podwójnym opakowaniu musielibyśmy wywołać dwa razy taką funkcję czyli kolejne silnia = dekorator(silnia)
silnia = dekorator(silnia)
# rekurencyjnie wykonuje się funkcja opakowanie()
silnia_wyn = silnia(5)
print("silnia_wyn:", silnia_wyn)

# funkcje możemy dekorować wielokrotnie, dekorator_2 będzie najbardziej na zewnątrz
#@dekorator_2
# tutaj jest wykonywany dekorator na sumatorze
@dekorator
def sumator(a, b):
    return a + b

# tutaj pod sumatorem mamy już udekorowaną funkcję
sumator_wyn = sumator(2, 17)
print("sumator_wyn:", sumator_wyn)
