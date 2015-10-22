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

# parametry z wartością domyślną (opcjonalne)
def dodawator(l1 = 1, l2 = 2):
    # takie przypisanie zastępuje zarówno domyślny, jak i podany w wywołaniu argument
    # l1 = 10
    return l1 + l2

print(dodawator())
print(dodawator(6))
print(dodawator(6, 7))
# przy podaniu nazw nie jest istotna kolejność
# jeśli podamy najpierw z nazwy, a potem pozycyjny - nawet jeśli jest opcjonalny, to nie zadziała
# dodawator(l1 = 3, 7)
print(dodawator(l2 = 15))

# najpierw obowiązkowe, potem domyślne; nie można mieszać
def mnoznikator(l1, l2 = 10):
    return l1 * l2

print(mnoznikator(10))
print(mnoznikator(10, 20))

# args i kwargs to są dowolne nazwy (może być foo i bar, spam i eggs)
# kwargs = key word args
# rozpakowanie dodatkowych argumentów do krotki - args i słownika - kwargs
# * rozpakowuje zwykłe argumenty do listy
# ** rozpakowuje nazwane argumenty do słownika
def funkcyjka(par1, par2 = 5, *args, **kwargs):
    # funkcja robi nic
    #pass
    print(par1)
    print(par2)
    print(args)
    print(kwargs)
    return None

funkcyjka(1)
funkcyjka(1, 2)
funkcyjka(1, 2, 3)
funkcyjka(1, 2, 3, 4, 5, 6, "gulci is the best")
# wartości opatrzone nazwą argumentu lądują w słowniku kwargs
funkcyjka(1, 2, 3, 4, 5, 6,
    slogan = "gulci is the best",
    rule = "python rulez")
# po kwargsach nie możemy już podawać argumentów do args
#funkcyjka(1, 2, 3, 4, 5, abc = "abc", "def")

lnum = (1, 2, 3, 4, 5)
# krotka jest pierwszym argumentem
funkcyjka(lnum)
# następuje rozpakowanie krotki, kolejne jej elementy są kolejnymi argumentami przekazanymi do funkcji, lądują w args
funkcyjka(*lnum)

dnum = {"par1" : 10, "par2" : 15, "tekst" : "gulci is the best"}
# rozpakowanie słownika, kolejne argumenty lądują w kwargs
funkcyjka(**dnum)

# parametry domyślne możemy pominąć
dnum = {"par1" : 10, "tekst" : "gulci is the best"}
funkcyjka(**dnum)

# przy takim przekazaniu cały słownik jest pierwszym argumentem
funkcyjka(dnum)

# rozpakowujemy dwie struktury za jednym razem
# trzeba pamiętać, żeby w słowniku nie były zdublowane parametry obowiązkowe i opcjonalne, bo te mogą zostać pozyskane wcześniej z listy
# ważna jest kolejność, najpierw zwykłe wartości, a potem nazwane
dnum = {"tekst1" : "hello", "tekst2" : "world"}
funkcyjka(*lnum, **dnum)

# przekształcamy krotkę na listę - jeśli chcemy zmodyfikować listę argumentów
list_num = list(lnum)
print(list_num)

# możemy rozpakować listę do funkcji, we wnętrzu i tak dostaniemy krotkę
funkcyjka(*list_num, **dnum)

# type jest klasy type, w py wszystko jest obiektem, więc funkcja type też nim jest
print(type(type))
