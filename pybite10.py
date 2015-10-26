# coding: utf-8

# jeśli otwieramy do odczytu i plik nie istnieje dostaniemy FileNotFoundError

# kasuje plik lub go tworzy
# plik = open("test.txt", "w")

# tworzy nowy plik, wyrzuca FileExistsError; py3
# plik = open("test.txt", "x")

# ustawia się na końcu pliku
# plik = open("test.txt", "a")

# + możliwość read/write
# domyślnie rt, t - text mode

# odczyt + zapis, r+, i wtedy ustawia się na początku

# r+b odczyt i zapis binarnego pliku

# fizyczny zapis do pliku, nie zamyka pliku, wyrzuca bufor na dysk
# plik.flush()

# jeśli plik jest otwarty do zapisu, to dopiero close() opróżnia bufor i zapisuje do pliku
# plik.close()

plik = open("test.txt", "w")

# zwraca liczbę zapisanych bajtów
# print(plik.write("gulci ma kota"))

# wypisuje None
# potrzebuje czegoś iterowalnego (np. generatora, listy)
print(plik.writelines("gulci ma kota\n"))
print(plik.writelines(str(i) + "|" for i in range(10)))

print(plik.closed)
print(plik.encoding)
# traktowanie błędów pliku
print(plik.errors)
# sprawdza czy plik jest konsolą; w lin konsolę można traktować jako plik i pisać do niej
print(plik.isatty())
print(plik.mode)
print(plik.name)
# sposób traktowania nowych linii
# None dla plików otwartych w sposób inny niź uniwersalny
print(plik.newlines)
print(plik.readable())
print(plik.writable())
print(plik.seekable())

# garbage collector py powinien zamknąć plik

plik.close()

# mamy automatyczne zamknięcie pliku
# jeśli w środku dostaniemy wyjątek, to with powinien zadbać o zamknięcie pliku
with open("test.txt") as plik:
    # dostaniemy listę linii w pliku (linie wraz ze znakiem końca linii)
    print(plik.readlines())
    # writelines() może przyjąć iterowalny element, np. listę, ale nie wymaga znaków końca linii, można sobie zlepić tekst

plik = open("test.txt", "r+")

# plik działa jak taśma, po read() jesteśmy na końcu pliku i nic już nie odczytamy
print(plik.read())
print(plik.read())

# przesuwamy się na początek pliku (lub w wybrane miejsce - bajt) i znów możemy coś odczytać
plik.seek(10)

# gdzie jesteśmy
print(plik.tell())
print(plik.read())
print(plik.tell())

plik.seek(0)
# odczytujemy do pierwszego znaku końca linii (włącznie z nim)
# znacznik ustawia się na następnym znaku
print(plik.readline())
print(plik.tell())

# plik otwarty z "w" będzie cały ucięty (truncate) - od seek(0)
# z truncate() można korzystać samodzielnie
plik.seek(10)
# plik.truncate()

plik.seek(0)
print(plik.read())

plik.close()
