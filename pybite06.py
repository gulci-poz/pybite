# coding: utf-8

# generatory

# generator pozwala stworzyć nieskończoną liczbę elementów w kontrolowany sposób
# range() jest generatorem
# w py2 był gerator i jeszcze jeden, który zwracał listę

print(list(range(10)))

# yield zwraca wartość, funkcja nadal działa, ale jest zawieszona
def gen_calkowite(n = 0):
    while n < 100:
        print("before")
        yield n
        print("after")
        n += 1

# zwraca obiekt generatora, musimy go jakoś zapamiętać
print(gen_calkowite())

x = gen_calkowite()

print(x.send(None))
print("przerwa")
# działanie generatora jest przerywane po wywołaniu yield
# startuje po ponownym zarządaniu wartości - kolejne wysłanie send(None)
print(x.send(None))

#for i in x:
#    print(i, end = ' ')

# przejście do nowej linii po pętli
#print()

# jednolinijkowiec opakowany w funkcję
def greeting(name = ''):
    print("Witaj,", input("Podaj imię: ") if not(name) else name)

greeting()
