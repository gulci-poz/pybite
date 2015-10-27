# coding: utf-8

# klasa to samodzielnie tworzony typ
# możemy pominąć object
# class NaszaKlasa:
class NaszaKlasa(object):
    # współdzielony między obiektami danej klasy
    atrybut_klasy = 7

    # konstruktor, dodajemy *args i **kwargs do najbardziej minimalistycznego wywołania
    # self to tworzony właśnie obiekt (wskaźnik), na początku to pusty obiekt podany do konstruktora
    def __init__(self, *args, **kwargs):
        """
        Konstruktor klasy
        """
        pass

class Osoba:
    ile_osob = 0

    def __init__(self, imie = "Bezimienny", wiek = 31):
        # atrybut obiektu
        self.imie = imie
        #self.imie = imie or input("Podaj imię > ")

        self.wiek = wiek

        # trzeba się odwoływać za pomocą nazwy klasy
        # inaczej będziemy się odwoływać do nieistniejącej zmiennej lokalnej
        Osoba.ile_osob += 1

    def metoda():
        # można zdefiniować funkcję wewnątrz funkcji
        # zwracamy funkcję;
        # podstawa działania dekoratorów (opakowywanie metod)
        def funkcja(parametr):
            return parametr + 1
        return funkcja

    def __del__(self):
        """
        Destruktor klasy
        """
        # Komunikat się pojawi przy usuwaniu obiektu przez garbage collector
        # nie mamy pewności, że obiekt zostanie usunięty
        print("{0} Koniec".format(self.imie))

    # można tworzyć klasy wewnątrz klasy, do potrzeb wewnętrznych
    class Wewn:
        pass

os1 = Osoba("gulci", 32)
os2 = Osoba("karolcia")

print(os1)
print(os1.imie)
print(os1.wiek)
print(os2)
print(os2.imie)
print(os2.wiek)
print(Osoba.ile_osob)

# isinstance() wykrywa również subklasy, np. przy dziedziczeniu
print("isinstance:", isinstance(os1, Osoba))
print("type:", type(os1))

print("hasattr:", hasattr(os1, "ile_osob"))

attr = getattr(os1, "ile_osob")
print("getattr:", attr)

# do atrybutu klasy da się odwołać za pomocą obiektu
# tak naprawdę każdy obiekt ma atrybut ile, który jest powiązany z atrybutem klasy ile, po każdej zmianie następuje aktualizacja
#print(os1.ile_osob)
#print(os2.ile_osob)

# kolejność sprawdzania metod do wywołania
print(Osoba.mro())

# w momencie przypisania wartości pod ile_osob dla wybranego obiektu
# ile_osob w tym obiekcie nie będzie już wskazywał na atrybut klasy
# powstanie atrybut obiektu
# os2 cały czas ma wskaźnik na aktrybut klasy, tam nie naspisywaliśmy wartości
os1.ile_osob = 0
print(Osoba.ile_osob)
print(os1.ile_osob)
print(os2.ile_osob)

del os1
del os2

# 6 - 31 min 45 sek
