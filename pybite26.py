# coding: utf-8

# metaklasy - klasy, których instancjami są klasy
# type - najbardziej pierwotna metaklasa
# type jest swoją własną metaklasą

class Moja(object):
    pass

obj = Moja()

# id to adres obiektu w pamięci
print("obj", id(obj))
print("Moja", id(Moja))

print("obj", type(obj))
print("Moja", type(Moja))

print("type", type(type))
