# coding: utf-8

# formatowanie

imie = "Sebastian"
nazwisko = "Gulczyński"

# możemy łatwo przestawiać zmienne do podstawienia w tekście
# odwołujemy się do nich za pomocą klucza i podajemy na końcu słownik zamiast krotki (krotka zmusza nas do zachowania kolejności)
# wartość przed typem rezerwuje przestrzeń do wyświetlenia
print("Uczeń %(imie)15s %(nazwisko)15s" % {"imie": imie, "nazwisko": nazwisko})

# w słowniku (lub krotce) można podać wartości, nie trzeba korzystać ze zmiennych
print("Stopień wtajemniczenia: %(exp)s" % {"exp": "asior"})

# jeśli jest jeden argument lub jeśli są w kolejność to wystarczy klamra
print("imię: {}".format(imie))
print("imię: {}; nazwisko: {}".format(imie, nazwisko))

# można przestawiać numery
print("nazwisko: {1}; imię: {0}".format(imie, nazwisko))

print("nazwisko: {nazwisko}; imię: {imie}"
    .format(imie = "Jan", nazwisko = "Kowalski"))

# takim przypadku nie możemy się odwoływać za pomocą indeksu
#print("nazwisko: {1}; imię: {0}"
#    .format(imie = "Jan", nazwisko = "Kowalski"))

dane = {"imie": "Jan", "nazwisko": "Kowalski"}

# rozpakowanie słownika
print("imię: %(imie)s; nazwisko: %(nazwisko)s" % dane)
print("imię: {imie}; nazwisko: {nazwisko}".format(**dane))

# rezerwowanie ilości miejsc w notacji z użyciem format() - sprawdzić
