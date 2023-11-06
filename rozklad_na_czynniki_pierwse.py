def rozklad(n):
    k = 2
    while n > 1:
        while n % k == 0:
            print(k)
            n = n / k
        k = k + 1

n = int(input("Podaj liczbę n: "))
print("Czynniki pierwsze", n, "to:")
rozklad(n)
