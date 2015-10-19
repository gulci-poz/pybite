#!/usr/bin/env python3
# coding: utf-8

# hashbank, tylko w lin, jeśli chcemy uruchamiać skrypty bez podania interpretera
# plik musi być do uruchomienia
# wersja kodowania dla py3, działa też w py2

def print_me(txt):
    # działa w py3 dla unicode, w py2 też działa
    """Drukowanie tekstu podanego przez użytkownika w wywołaniu funkcji"""
    print(txt)

print_me("Cześć!")
