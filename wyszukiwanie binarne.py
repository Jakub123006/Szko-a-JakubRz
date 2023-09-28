def wyszukiwanie_binarne(wyszukiwana, tab):
    l = 0
    w = 15

    while l <= w:
        sr = (l + w) // 2
        if tab[sr] == wyszukiwana:
            return sr
        elif tab[sr] > wyszukiwana:
            w = sr - 1
        else:
            l = sr + 1

    return -1

tablica = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
wyszukiwana_liczba = 18
wynik = wyszukiwanie_binarne(wyszukiwana_liczba, tablica)

if wynik != -1:
    print(f"Szukana liczba {wyszukiwana_liczba} jest na pozycji {wynik}.")
else:
    print(f"Szuklana liczba {wyszukiwana_liczba} Nie ma jej na tablicy.")