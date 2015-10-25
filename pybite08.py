# coding: utf-8

# idiom as
#from coś import coś as coś

name = None

# idiom is
if name is None:
    pass

# idiom or
print(name or "brak imienia")

name = input("Podaj imię: ")

# idiom - przypisanie ze sprawdzeniem warunku
num = 32 if name == "gulci" else 0

print(name)
print(num)

# mamy jeszcze idiom for dla wypełnienia listy, było w pybite07.py - Fahrenheit
