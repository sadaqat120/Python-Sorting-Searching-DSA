def gcd(a1, a2):
    while a2 != 0:
        hcf = a1 % a2
        a1 = a2
        a2 = hcf
    return a1


print(gcd(70, 28))
