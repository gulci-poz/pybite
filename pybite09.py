# coding: utf-8

vals = ["gulci", 3.14, 32]

# idiomy - krótkie zapisy, które potrafią zrobić duże rzeczy

# idiom in

print("42 in list:", 42 in vals)
print("4 in list:", 32 in vals)

dvals = {"jeden" : 1, "dwa" : 2, "trzy" : 3}

# in w słownikach sprawdza po kluczach, można też użyć keys() i values()
print(2 in dvals.values())
print("dwa" in dvals)
print("dwa" in dvals.keys())

# sprawdzenie wystąpienia odpowiadających sobie elementów
print(("dwa", 2) in dvals.items())

# nowy słownik o kluczach wyciągniętych z iterowalnego elementu
# trzeba zrobić przypisanie, fromkeys() domyślnie nie zapisuje
new_dict = {}
new_dict = new_dict.fromkeys(range(10), "gul")
print(new_dict)

# składanie / comprehension list i słowników

# składanie listy

db_list = [
    {"imie" : "Sebastian", "id" : 1},
    {"imie" : "Karolina", "id" : 2},
    {"imie" : "Wiktoria", "id" : 3},
    {"imie" : "Melania", "id" : 4}
]

print(db_list)

#imiona = []

#for d in db_list:
#    imiona.append(d["imie"])

# lub krócej

# w środku mamy tak naprawdę generator, możemy dołożyć warunek, else nie działa
imiona = [d["imie"] for d in db_list if d["id"] % 2 == 1]

print(imiona)

# składanie słownika

# i to id wzięte z indeksu listy, d to element listy - tutaj słownik
db_dict = {i : d["imie"] for i, d in enumerate(db_list)}
print(db_dict)

# mamy obiekt enumerate
# zawiera on krotki z złożone z id z listy i ze słownikami z listy
enum_list = enumerate(db_list)
print(enum_list)

for elem in enum_list:
    print(elem)

# lambda - szybkie definiowanie krótkich funkcji

#lambda x, y: x + y

# nie posortujemy obiektów - słowników
# key przyjmuje funkcję, która wskazuje według czego będzie sortowanie
# sort() zapisuje rezultat do tej samej listy
# drukujemy listę, a nie rezultat sort()
print(db_list)
db_list.sort(key = lambda d: d["imie"])
print(db_list)

# można zapisać funkcję, zmienna będzie typu funkcja
sort_imie = lambda d: d["imie"]
print(type(sort_imie))
