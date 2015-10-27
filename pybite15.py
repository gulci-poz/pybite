# coding: utf-8

# importy najlepiej na górze i to alfabetycznie

# przy imporcie wypisze tę linijkę (nazwę modułu)
print(__name__)

def start():
    print("Cześć, jestem programem!")
    return 0

# _ metoda do wewnętrznego użytku
# __ metoda do specjalnego użytku w py
# nazwa modułu nie może być "import" ani "test"

# jeśli wykonujemy jako program
if __name__ == "__main__":
    start()
else:
    print("Jestem modułem")

# jako package dla modułu możemy użyć folderu
# tworzymy tam sobie plik __init.py__
# może być pusty lub może zawierać np. deklaracje klas (pełni rolę hipotetycznego pliku py dla package)
# dla py3 nie jest to konieczne
