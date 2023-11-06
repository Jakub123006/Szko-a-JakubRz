def potegowanie_szybkie(a, n):
    w = 1  

    while n > 0: 
        if n % 2 == 1:  
            w *= a  

        a *= a 
        n //= 2  

    return w  

 
a = int(input("podaj podstawę: "))
n = int(input("podaj potęgę: "))

wynik = potegowanie_szybkie(a, n)
print(f"{a}^{n} = {wynik}")