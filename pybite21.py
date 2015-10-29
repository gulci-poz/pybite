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
    # można tutaj wyrzucić wyjątek (pójdzie wyżej), pojawi się po wykonaniu try
    raise
# else się wykonuje, jeśli pozostałe wyjątki nie wystąpiły
else:
    print("Jestem w else.")
# finally zawsze się wykonuje
# tutaj sprzątamy, np. usuwamy obiekty
finally:
    print("Jestem w finally.")

print("Po wszystkim.")

# 7 - 1 g 6 min
