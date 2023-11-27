def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)

n = int(input("Podaj liczbę n: "))
wynik = silnia(n)
print(f"{n}! = {wynik}")