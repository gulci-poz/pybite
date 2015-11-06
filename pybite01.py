# -*- coding: utf-8 -*-

# __future__ to "missing compatibility layer between py2 and py3"
# umożliwia użycie kodu py3 dla py2 i py3

# literały w Python 3000
from __future__ import unicode_literals, absolute_import

#print będzie funkcją
from __future__ import print_function

#dzielenie będzie rzeczywiste, // da nam wynik ze starego dzielenia
from __future__ import division

# będzie można używać with
from __future__ import with_statement

# jeśli plik py jest importowany jako moduł, to specjalna zmienna __name__ przyjmie nazwę tego modułu
# jeśli plik py ma być interpretowany, a nie importowany, to __name__ przyjmie wartość "__main__" i nastąpi interpretowanie pliku
# przypisanie do zmiennej __name__ ma miejsce przed importem (wykonaniem)
# ten warunek można też zapisać inaczej, np. dać komunikat
#if __name__ == "__main__":
#main()

# ipython podpowiada składnię, można aktualizować przez pip
# stary input() pozwalał wprowadzić wyrażenie, które było interpretowane
# openstack
# openshift

# przy włączonym imporcie z __future__ trzeba stosować funkcję print()

# obiekt __builtin__ istnieje w py2
#import __builtin__

# dla py3
#import builtins

import keyword

# rzutowanie na liczbę zespoloną
print(complex(4))

# rzutowanie na 0 i Null daje 0 (False), rzutowanie na inną wartość daje 1 (True)
print(bool(1))
print(bool(-1))
print(bool(0))
print(bool(None))

# oznaczenie pustej wartości None - jak null lub nil
print(type(None))

# następuje rzutowanie do nadrzędnego typu
print(3.0 + 4)

# będzie 1
print(True + False)

# można mieć zmienną z polskimi znakami
imię = "Sebuś"
# można, ale tylko w py3, w py2 będzie SyntaxError

# zwraca wynik dzielenia całkowitego i resztę modulo
print(divmod(3, 2))

# ** działa też jako pierwiastkowania
# w py2 trzeba dać przecinek i zero, bo inaczej wynik dzielenia będzie 0 (obcięcie do 0), a 8 do zerowej to 1
print(8 ** (1/3))

# istnieje tryb decimal, jest dokładniejszy

# dla py2
#print dir(__builtin__)

# zastrzeżone ciągi znaków
#print(dir(builtins))

# zastrzeżone słowa kluczowe
print(keyword.kwlist)

print(keyword.iskeyword('break'))

# w py3 można coś przypisać do print, to funkcja, potem nie wykonamy print
# w py3 print nie jest słowem kluczowym, w py2 - jest
# będzie inna lista w py2 i py3
