# coding: utf-8

lista = [1, 2, 3]

try:
    print(lista[3])

    # try można zagnieżdżać

# nie piszemy pustego except, bo będziemy przyjmowali każdy wyjątek
# except Exception - to samo, co pusty wyjątek; od tej klasy rozpoczynamy pisanie swoich wyjątków, najpierw korzystamy z dostępnych wbudowanych wyjątków

except IndexError:
    print("ERROR!")


class MyOwnException(Exception):
    pass

# wyrzucanie wyjątków
#raise MyOwnException("Mój ERROR")

# skrótowe wyrzucanie AssertionError, tu nie zdefiniujemy własnej klasy
#assert 1 == 0, "ERROR"


try:
    print(lista[3])
except MyOwnException:
    print("Błąd MyOwnException")
except IndexError:
    print("Brak indeksu")
    # obsługujemy wyjątek na ile to możliwe
    # można potem wyrzucić wyjątek (pójdzie wyżej), pojawi się po wykonaniu try
    # dobry sposób na zakończenie programu, gdy doszliśmy do oczekiwanego wyniku, jesteśmy wewnątrz zagnieżdżonej struktury i nie potrzebujemy kończyć jej wykonywania (zamiast bawić się w break), np. raise "ItemFound" - mamy oczekiwany wynik, obsługujemy wyjątek, wyrzucamy go i wyskakujemy z programu (błąd: operacja zakończona powodzeniem)
    # jeśli wyjątek nie będzie obsłużony, to będzie się piął coraz wyżej w hierarchi programu aż w końcu zostanie zgłoszony do procesu głównego i program w końcu się wywali

    # dajemy raise gdzieś w try, po zakończeniu obliczeń, tutaj wywalimy program
    #raise

# else się wykonuje, jeśli pozostałe wyjątki nie wystąpiły
else:
    print("Jestem w else.")

# finally zawsze się wykonuje
# tutaj sprzątamy, np. usuwamy obiekty
finally:
    print("Jestem w finally.")

print("Po wszystkim.")

##################################################

class ItemFound(Exception):
    pass

try:
    for i in range(0, 100):
        for j in range(0, 300):
            for k in range(3, 500):
                if k == j ** i:
                    raise ItemFound()
                    # wyrzucamy wyjątek, który potem jest obsłużony

except ItemFound as e:
    # mamy dostęp do obiektu wyjątku za pomocą e, możemy to zapisać do logu
    # --> logging facility for python

    print("found i j k:", i, j, k)

    # tutaj nie dajemy raise, chyba że chcemy wywalić program
