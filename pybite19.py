# coding: utf-8

class Punkt:
    def __init__(self, x, y):
        """
        Parametry:
        x, y - współrzędne punktu
        """
        self.x = x
        self.y = y

    # napisowa reprezentacja obiektu
    # uruchamia się w momencie rzutowania obiektu na napis, np. w print
    def __str__(self):
        # można zostawić dwa returny, kolejne po pierwszym będą zignorowane
        #return "Punkt o współrzędnych x = %.2f; y = %.2f" % (self.x, self.y)
        #return "Punkt o współrzędnych x = {0}; y = {1}".format(self.x, self.y)

        # wykorzystanie punktu do formatowania, w napisie możemy korzystać z atrybutów
        return "x: {pkt.x}; y: {pkt.y}".format(pkt = self)

    # "oficjalna" reprezentacja obiektu; jeśli wypiszemy zmienną w trybie interaktywnym - bez print() lub korzystając z repr()
    def __repr__(self):
        return "coord > x: {pkt.x}; y: {pkt.y}".format(pkt = self)

    # przeładowanie operatorów

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __add__(self, other):
        pass

    def odl_od_punktu(self, punkt):
        # punkt - inny obiekt Punkt
        odl = ((self.x - punkt.x) ** 2 + (self.y - punkt.y) ** 2) ** 0.5
        return odl

    def odl_od_centrum(self):
        # odległość od (0, 0)
        # trzeba pamiętać o self, odwołujemy się do metody z naszej klasy
        return self.odl_od_punktu(Punkt(0, 0))

class Odcinek:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __add__(self, other):
        pass
        #return dodawanie
        # możemy potem używać operatora +
        # odcinek1 + odcinek2

    def __len__(self):
        pass
        #return dlugosc

    def __int__(self):
        return self.__len__(self)

    def __mul__(self, other):
        pass
        # może być mnożenie skalarne (długość x długość) lub wektorowe (powstaje nowy wektor); może być też mnożenie wektora przez skalar
        # spróbować zaimplementować

pkt1 = Punkt(1.4, 2.15)
print(pkt1)

# tak wypiszemy w trybie interaktywnym, korzystając z __repr__()
#pkt1

# korzysta z __str__()
print("{}".format(pkt1))

# korzysta z __repr__()
print("{}".format(repr(pkt1)))
