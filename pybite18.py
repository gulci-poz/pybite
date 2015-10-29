# coding: utf-8

class Punkt:
    def __init__(self, x, y):
        """
        Parametry:
        x, y - współrzędne punktu
        """
        self.x = x
        self.y = y

    def odl_od_punktu(self, punkt):
        # punkt - inny obiekt Punkt
        odl = ((self.x - punkt.x) ** 2 + (self.y - punkt.y) ** 2) ** 0.5
        return odl

    def odl_od_centrum(self):
        # odległość od (0, 0)
        # trzeba pamiętać o self, odwołujemy się do metody z naszej klasy
        return self.odl_od_punktu(Punkt(0, 0))

class Kolo:
    def __init__(self, centrum, r):
        """
        Parametry:
        centrum - środek koła, obiekt klasy Punkt
        r - promień koła
        """
        self.r = r
        self.cntr = centrum

    def czy_wewnatrz(self, punkt):
        return self.cntr.odl_od_punktu(punkt) < self.r

class Prostokat:
    def __init__(self, wierzch1, wierzch2):
        """
        wierzch1 - współrzędne punktu lewego górnego, obiekt klasy Punkt
        wierzch2 - współrzędne punktu prawego dolnego, obiekt klasy Punkt
        """
        self.wierzch1 = wierzch1
        self.wierzch2 = wierzch2

    def czy_wewnatrz(self, punkt):
        return (punkt.x > self.wierzch1.x
            and punkt.y < self.wierzch1.y
            and punkt.x < self.wierzch2.x
            and punkt.y > self.wierzch2.y)

    def pole(self):
        self.wierzch3 = Punkt(self.wierzch1.x, self.wierzch2.y)
        self.bok_a = self.wierzch1.odl_od_punktu(self.wierzch3)
        self.bok_b = self.wierzch2.odl_od_punktu(self.wierzch3)
        self.pole_pow = self.bok_a * self.bok_b
        return self.pole_pow

class Odcinek:
    def __init__(self, wierzch1, wierzch2):
        """
        wierzch1 - współrzędne pierwszego punktu odcinka, obiekt klasy Punkt
        wierzch2 - współrzędne drugiego punktu odcinka, obiekt klasy Punkt
        """
        self.wierzch1 = wierzch1
        self.wierzch2 = wierzch2

    def czy_przecina(self, odc):
        pass
        # dokończyć
        #return tak_nie

##################################################

pkt1 = Punkt(0, 0)
pkt2 = Punkt(0, 0)

print(pkt1)
print(pkt2)
print(pkt1 is pkt2)

pkt1 = pkt2
print(pkt1 is pkt2)

# pkt1 nie podąża za zmianami pkt2 (lista - tak)
pkt2 = Punkt(0, 0)
print(pkt1 is pkt2)

# różne obiekty, można porównywać atrybuty
print(pkt1 == pkt2)

pkt3 = Punkt(11, 7)
pkt4 = Punkt(23, 3)

print(pkt3.odl_od_centrum())
print(pkt4.odl_od_centrum())

print(pkt3.odl_od_punktu(pkt4))
print(pkt4.odl_od_punktu(pkt3))
print(pkt3.odl_od_punktu(pkt1))
print(pkt4.odl_od_punktu(pkt1))

kolo1 = Kolo(Punkt(3, 4), 5)
print(kolo1.czy_wewnatrz(Punkt(5, 7)))
print(kolo1.czy_wewnatrz(Punkt(50, 50)))

prostokat1 = Prostokat(Punkt(2, 6), Punkt(8, 1))
print("in rect:", prostokat1.czy_wewnatrz(Punkt(3, 5)))
print("out rect:", prostokat1.czy_wewnatrz(Punkt(9, 5)))
print("pole:", prostokat1.pole())

del pkt1
del pkt2
del pkt3
del pkt4
del kolo1
del prostokat1
