# coding: utf-8

# liczba argumentów w definicji i wywołaniu musi się zgadzać
def zrob_cos():
    print("Robię coś.")
    return 155

zrob = zrob_cos()
print(zrob)

# nie ma przeciążania nazw funkcji
# scope lokalny dla zmiennych w funkcji

# global tutaj nic nie zmienia, argument i tak na czas wykonywania funkcji zastąpi tę wartość; ten global miałby sens, jeśli to by była podczęść czegoś (np. jeśli to by było wnętrze funkcji)
# z globalizacją schodzimy w dół, trzeba ją deklarować przed użyciem zmiennej w danym scope
# global i
i = 7
k = "krowa"
print(k)

# i jest przysłaniane przez i podane przy wywołaniu
# czyli to jest lokalne i
def moja_funkcja(i, j):
    # globalizuję w tym scope przed użyciem zmiennej
    global k
    # nie mogę zglobalizować i, bo jest już parametrem
    # global i
    k = "pies"
    return i + j

print(moja_funkcja(5, 10))

# i wraca do pierwotnej wartości
print(i)

# k było globalne funkcji, zostaje zmienione
print(k)

lista_arg = [1, 2, 3, 4, 5]

def lista_mod(liczby):
    # przypomnienie - rozszerzamy o coś iterowalnego, a append() wymaga jednego argumentu
    lista_arg.extend([6, 7, 8, 9])

lista_mod(lista_arg)

# lista jest przekazywana przez referencję
print(lista_arg)

# parametry domyślne (opcjonalne)
def dodawator(l1 = 1, l2 = 2):
    # takie przypisanie zastępuje zarówno domyślny, jak i podany w wywołaniu argument
    # l1 = 10
    return l1 + l2

print(dodawator())
print(dodawator(6))
print(dodawator(6, 7))

#  3 - 39 min
