# coding: utf-8

# mixin, mała klasa implementująca jedną funkcjonalność, nie trzeba od razu implementować całego dużego rozwiązania, potem takie klasy się łączy

class Osoba(object):
    def __init__(self, imie, nazwisko):
        # jeśli istniałyby atrybuty klasy o takiej samej nazwie, to te atrybuty je nadpiszą dla danego obiektu (tutaj akurat dla każdego obiektu, bo nadpisalibyśmy w konstruktorze)
        # nadal byłby dostęp do atrybutów klasy, ale nie odwołując się z obiektu, tylko z samej klasy Osoba.atrybut_klasy
        self.imie = imie
        self.nazwisko = nazwisko

    def przywitanie(self):
        print("Hej, człowieku!")

class Zwierzak(object):
    def przywitanie(self):
        print("Hej, zwierzaku!")

class Roslinka(object):
    def przywitanie(self):
        print("Hej, roślinko!")

class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, stanowisko):
        # w py3 wystarczy
        # kolejność przeszukiwania dla dziedziczenia jest w kolejności podanych klas w nagłówku (mro), od lewej; dotyczy też atrybutów klasy
        super().__init__(imie, nazwisko)

        # w py2 i dla purystów
        #super(Pracownik, self).__init__(imie, nazwisko)

        # analogiczne wywołanie
        # wbrew zalecenion twórców języka
        # odwołujemy się bezpośrednio do nazwy klasy
        # jeśli dziedziczymy z kilku klas i chcemy implementację __init__ z konkretnej klasy, to możemy użyć tej notacji
        #Osoba.__init__(self, imie, nazwisko)

        self.stanowisko = stanowisko

# mamy kolejność dla metod (Method Resolution Order - mro):
# Student, Zwierzak, Roslinka, Osoba, object
class Student(Zwierzak, Roslinka, Osoba):
    def __init__(self, imie, nazwisko, srednia = 5):
        super().__init__(imie, nazwisko)
        self.srednia = srednia

    def przywitanie(self):
        super().przywitanie()

prac1 = Pracownik("Jan", "Kowalski", "portier")
print(prac1.imie)
print(prac1.nazwisko)
print(prac1.stanowisko)

stud1 = Student("Tomasz", "Iksiński")
print(stud1.imie)
print(stud1.nazwisko)
print(stud1.srednia)
stud1.przywitanie()
# tu mamy od lewej kolejność klas dla wyboru metod
print(Student.mro())

print("Pracownik Pracownik:", isinstance(prac1, Pracownik))
print("Pracownik Osoba:", isinstance(prac1, Osoba))
print("Pracownik object:", isinstance(prac1, object))

print("Student Student", isinstance(stud1, Student))
print("Student Zwierzak", isinstance(stud1, Zwierzak))
print("Student Roslinka", isinstance(stud1, Roslinka))
print("Student Osoba", isinstance(stud1, Osoba))
print("Student object", isinstance(stud1, object))
