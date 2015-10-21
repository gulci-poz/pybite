# coding: utf-8

# for to tak naprawdę foreach w py
# numeryczny iterator w for
# drukuje od 0 do 9
for i in range(10):
    print(i)
else:
    # to może być odczytane jako finally
    # w if else może robić za default
    # jeśli pętla się nie wykona, to ten blok i tak się wykona
    # jeśli pętla będzie przerwana break, to ten blok się nie wykona
    # else działa również z while
    print("Koniec pętli")

# prosty sposób na zamianę wartości zmiennych, bez użycia zmiennej tymczasowej
# rozpakowywanie krotki (tuple unpacking)
a, b = 10, 15
print(a, b)

a, b = b, a
# to samo (a, b) = (b, a) mamy do czynienia z krotką
print(a, b)

pi = 3.14
# 5 oznacza wszystkie cyfry, łącznie z przecinkiem i częścią ułamkową
print("Formatowanie %5.2f" % pi)

# odpowiednik empty_list = []
empty_list = list()
print(type(empty_list))

# ipython: empty_list? empty_list.append?

# dostaniemy listę znaków zawartych w tym stringu
another_list = list("Ala ma kota")
print(another_list)

# dodamy obiekt, tutaj string do listy
another_list.append("kot ma Alę")
print(another_list)

# dodajemy nową listę, która zawiera znaki z podanego stringa
another_list.append(list("wszyscy mają mambę"))
print(another_list)

# dodajemy każdy znak z nowej listy osobno
for sign in list("wszyscy mają mambę"):
    another_list.append(sign)

print(another_list)

# czyścimy listę
another_list.clear()
print(another_list)

# rozszerzamy listę o zawartość czegoś iterowalnego, np. innej listy
# w przypadku append() dodalibyśmy całą listę jako jeden element
another_list.extend(range(10))
print(another_list)
another_list.clear()
# a tak możemy zrobić z liczb stringi
another_list.extend(str(num) for num in range(10))
print(another_list)

another_list.sort()
print(another_list)

# remove() usuwa pierwsze wystąpienie elementu lub wyrzuca wyjątek
another_list.remove('5')
print(another_list)

# pop usuwa element z końca listy i zwraca go
another_list.pop()
print(another_list)

# można podać indeks
another_list.pop(2)
print(another_list)

# pop(-1) daje ten sam efekt co pop(), zdjęcie ostatniego elementu
# można odliczać indeksy od końca w dół
another_list.pop(-1)
print(another_list)

# -1 to ostatni element, i tak dalej od końca
print(another_list[-1])
print(another_list[-2])
print(len(another_list))

another_list.extend(another_list)
another_list.extend(another_list)
print(another_list)

# slices

# left included
print(another_list[2:5])

# trzeci argument to wartość kroku przemieszczenia
print(another_list[2:9:2])

# od początku
print(another_list[:9:2])

# do końca
print(another_list[2::2])

# co drugi element od początku do końca
print(another_list[::2])

# wycinek całej listy, kopia
print(another_list[:])

# można używać indeksów ujemnych
print(another_list[2:-2])
print(another_list[-5:-1])
# bez podania końca/początku, ta wartość końcowa/początkowa będzie wypisana
# można ustawiać krok ujemny
# wypisujemy całą listę wspak
# wystarczy podać ujemny krok, bez pozostałych wartości
print(another_list)
print(another_list[::-1])
# co drugi element od końca listy
print(another_list[::-2])

# sprawdzenie palindromu
word = "KAJAK"
print(word == word[::-1])

# tuples - krotki
# dostaniemy tylko nawiasy, bez przecinka
print(tuple())

# to jest liczba, nawias robi za operator
single = (4)
print(type(single))

# jednoelementowy tuple
single_tuple = (4,)
print(type(single_tuple))
print(single_tuple)

# krotkę definiuje przecinek, nawias tylko porządkuje
single_tuple_2 = 4,
print(type(single_tuple_2))
print(single_tuple_2)

# działają indeksy, indeksy ujemne, wycinki, można iterować
krotka = (1, 2, 3, "bla", "a", ["b", 1], 3)
print(krotka)

# nie można zmieniać wartości elementów krotki

# ilość wystąpień danej wartości
print(krotka.count(3))

# indeks pierwszego wystąpienia danej wartości
print(krotka.index(3))

# ale np. element listy będącej w krotce możemy zmienić
krotka[5][0] = 1
print(krotka)

# MRO - method resolution order
# klasa powstała z połącenia innych klas, dla instancji tej klasy MRO decyduje o kolejności rowiązywania klasy, jest to kolejność przeszukiwania klas pod kątem użytych atrybutów

print(tuple.mro())

# zamiana listy na krotkę, element musi być iterowalny
print(tuple(another_list))
print(tuple("gulci"))

# dictionary - tablica asocjacyjna

print(dict())
d = {}
print(d)
# klucze i wartości, klucz + wartość = item
d = {"Ala" : "kot", "Ola" : "pies"}
print(d)
# wypisuje bez cudzysłowia
print(d["Ola"])
imie = "Ala"
print(d[imie])
# można "ręcznie" dodać nowy element, w odróżnieniu od listy (tylko append())
d["gulci"] = "owczarek"
print(d["gulci"])

# dict nie jest sortowany, istnieje typ sorted_dict, trzeba go importować

# iterujemy po kluczach
for i in d:
    print(i, d[i])

# lista tuples (key, value) dict_items
print(d.items())

for i in d.items():
    print(i)

# pętla dwuwartościowa, key i value to elementy tuple
# to takie rozpakowywanie w pętli
for key, value in d.items():
    print(key, value)

# rozpakowanie - można używać innych typów, liczba wartości musi się zgadzać
a, b = ["Ala", "kot"]
print(a, b)

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [9, 8, 7, 6, 5]

# powstanie iterator - zip()
print(zip(l1, l2))

# rzutujemy iterator na listę
# powstanie lista krotek po skombinowaniu elementów na poszczególnych pozycjach, elementy nie do pary zostaną odrzucone
print(list(zip(l1, l2)))

for w1, w2 in zip(l1, l2):
    print(w1, w2)

# dict_keys, lista kluczy
print(d.keys())

# dict_values, lista wartości
print(d.values())

# można zmienić lub dopisać wartość, podajemy słownik, który jest porównywany z dotychczasowym słownikiem
d.update({"gulci" : "bernardyn", "Jacek" : "jamnik"})
print(d)

# ściąga losowo key i value, zwraca w postaci tuple
# przydatne w iteracyjnym niszczeniu słownika
# jeśli słownik jest pusty dostaniemy wyjątek KeyError
print(d.popitem())
print(d)

# usuwa klucz ze słownika i zwraca jego wartość, jeśli nie ma takiego klucza w słowniku, zwracany jest drugi argument (default), jeśli klucz nie istnieje i nie podamy default, to dostaniemy wyjątek KeyError
print(d.pop("Karolcia", "Nie ma Karolci"))

# wypisuje wartość, jak w odczycie przez indeks, ale jeśli wskazanego klucza nie ma w słowniku, to dostaniemy None, a nie błąd; można podać default
print(d.get("Wiki", "Nie ma Wiki"))

# działa jak get(), jeśli klucza nie ma, to dodaje go do słownika
# do tworzenia lub nadpisywania domyślnych ustawień
print(d.setdefault("Mela", "kaka"))
print(d)

# zbiory

# zwraca set()
print(set())

zb1 = set("Ala ma kota")
zb2 = set("Kot ma Alę")
zb3 = set("Ala ma kota i psa")

# powstaje słownik złożony ze znaków ze stringu, bez powtórzeń, w losowej kolejności
print(zb1)
print(zb2)

print(zb1.difference(zb2))
print(zb1.union(zb2))
print(zb1.intersection(zb2))
print(zb1.issubset(zb3))
print(zb3.issuperset(zb1))
print(zb1.issuperset(zb2))

li1 = [1, 2, 3, 4]
li2 = li1

print(li1)
print(li2)

li1[0] = 9
li2 = li1

# po przypisaniu wartość zmieniła się w obu listach, mamy do czynienia z referencją, uwaga przy przekazywaniu argumentów do funkcji - przekazujemy przez referencję
# etykieta = samoprzylepna kartka
print(li1)
print(li2)

# skolonowanie listy, wtedy nie ma referencji
another_list.copy()

# tutaj mamy kopiowanie listy za pomocą całościowego wycinka
another_list_2 = another_list[:]
