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

# 19 min
