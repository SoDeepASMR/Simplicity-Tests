import random, sympy, sys
import colorlabels as cl
from decimal import *


def gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def Test_Ferma(n: int) -> bool:
    for i in range(1000):
        g = random.randint(2, n - 1)
        if (g ** (n - 1)) % n != 1:
            return False
    return True


def Test_SSt(n: int) -> bool:
    for i in range(1000):
        a = random.randint(2, n - 1)
        g = ((n - 1) // 2)
        r = (a ** g) % n
        if gcd(a, n) > 1:
            return False

        if r != 1 and r != n - 1:
            return False

        if r % n != sympy.jacobi_symbol(a, n) % n:
            return False

    return True


def Test_MR(n: int) -> bool:
    def toBinary(j: int):
        r = []
        while j > 0:
            r.append(j % 2)
            j = j / 2
            return r

    def MillerRabin(m: int) -> bool:
        for j in range(1000):
            a = random.randint(1, m - 1)
            b = toBinary(m - 1)
            d = 1
            for i in range(len(b) - 1, -1, -1):
                x = d
                d = (d * d) % m
                if d == 1 and x != 1 and x != m - 1:
                    return False
                if b[i] == 1:
                    d = (d * a) % m
                    if d != 1:
                        return False
                    return True

    return MillerRabin(n)


def Tests(n: int) -> str:
    if Test_Ferma(n) == False: return f"{cl.RED}Число {cl.WHITE}{n} {cl.RED}составное (по тесту Ферма)"
    if Test_SSt(n) == False: return f"{cl.RED}Число {cl.WHITE}{n} {cl.RED}составное (по тесту Соловэя-Штрассена)"
    if Test_MR(n) == False: return f"{cl.RED}Число {cl.WHITE}{n} {cl.RED}составное (по тесту Миллера-Рабина)"
    return f"{cl.GREEN}Число {cl.WHITE}{n}{cl.GREEN} с большой вероятностью {cl.WHITE}{'простое'.upper()}"


num = int(sys.argv[1])
print(Tests(num))
