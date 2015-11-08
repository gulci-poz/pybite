from timeit import Timer, timeit
#from sys import getrecursionlimit
#from sys import setrecursionlimit
#from math import factorial
#from scipy.misc import factorial
#import numpy

def silnia_rek(n):
    if n == 0:
        wynik = 1
    else:
        n * silnia_rek(n-1)

def silnia_iter(n):
    wynik = 1
    while n >= 1:
        wynik = wynik * n
        n -= 1

##################################################

#silnia_iter
#silnia_czas = Timer(
    #"silnia_iter(1000000)",
    #"from __main__ import silnia_iter").timeit(number = 1)

#silnia_rek
#print("default recursion limit:", getrecursionlimit())
#setrecursionlimit(1500000)
#print("new recursion limit:", getrecursionlimit())

#silnia_czas = Timer(
    #"silnia_rek(1000000)",
    #"from __main__ import silnia_rek").timeit(number = 1)

#math.factorial
#silnia_czas = Timer(
    #"factorial(1000000)",
    #"from math import factorial").timeit(number = 1)

#scipy.math.factorial
#exact = True, korzystamy z long int
silnia_czas = Timer(
    "factorial(1000000, exact = True)",
    "from scipy.misc import factorial").timeit(number = 1)

#numpy.math.factorial
#silnia_czas = Timer(
    #"numpy.math.factorial(1000000)",
    #"import numpy").timeit(number = 1)

print("czas:", str(silnia_czas))

#wyniki
#silnia_iter: 735.90179016
#silnia_rek: segmentation fault (core dumped)
#math.factorial: 13.48458166699993
#scipy.misc.factorial: ?
#numpy.math.factorial: 13.484593997000047
