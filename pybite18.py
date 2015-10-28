# coding: utf-8

class Punkt:
    def __init__(self, x, y):
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
    def __init__(self, x, y, r):
        self.r = r
        self.cntr = Punkt(x, y)

    def czy_wewnatrz(self, punkt):
        return self.cntr.odl_od_punktu(punkt) < self.r

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

kolo1 = Kolo(3, 4, 5)
print(kolo1.czy_wewnatrz(Punkt(5, 7)))
print(kolo1.czy_wewnatrz(Punkt(50, 50)))

# 6 - 1 g 22 min
