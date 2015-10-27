# coding: utf-8

def wczytaj_od_usera():
    """
    Pobiera od użytkownika napis i zapisuje do pliku, działa do pojawienia się pustej linii
    """
    napis = input("Podaj napis do zapamiętania > ")

    with open("imiona", "a") as plik:
        while napis:
            plik.write(napis + "\n")
            napis = input("Podaj napis do zapamiętania > ")

def wczytaj_z_pliku():
    with open("imiona", "r") as plik:
        linijki = plik.readlines()
        # result jest dostępny w całej funkcji, nie tylko w with
        result = {idx + 1: linia.strip() for idx, linia in enumerate(linijki)}
    return result

#wczytaj_od_usera()
imiona_dict = wczytaj_z_pliku()
print(imiona_dict)

# SPHINX - tworzenie dokumentacji
# opiera się na reStructuredText, jest to w pewnym stopniu pochodna markdown
