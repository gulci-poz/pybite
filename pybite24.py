# coding: utf-8

class Klasa:
    def __init__(self):
        # prywatny element - co najmniej jeden podkreślnik
        # ipython przy wykonaniu introspekcji (kropka + Tab) nie pokazuje prywatnych elementów, trzeba dać _ i wtedy pokaże
        self._x = 1
        self.k = 32

    # ~getter
    # fget - self to pierwszy parametr property()
    # fset - val to drugi parametr property()
    # fdel
    # fdoc
    @property
    def x(self):
        print("pobieram _x")
        return self._x

    @x.setter
    def x(self, val):
        print("ustawiam _x na", val)
        self._x = val

    @x.deleter
    def x(self):
        print("kasuję k")
        del self.k

##################################################

obj = Klasa()

# mamy dostęp zarówno przez getter x(), jak i bezpośrednio przez wartość _x
#print(obj._x)
#print(obj.x())
# metoda klasy
#print(obj.x)

# można w locie stworzyć atrybut klasy
#obj.y = 10

# da się nadpisać atrybut klasy
#Klasa.x =

# po udekorowaniu funkcją property @property
print(obj.x)

# użycie settera
obj.x = 55
print(obj.x)

# użycie deletera
print(obj.k)
print("hasattr k:", hasattr(obj, "k"))
del(obj.x)
print("hasattr k:", hasattr(obj, "k"))
# tu atrybut k jest już usunięty
#print(obj.k)

# 7 - 1 godz.

# flask
# py - fluent, objects
# agile --> stx next
