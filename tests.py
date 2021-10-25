import random, sympy, sys
import colorlabels as cl


def gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def Test_Ferma(n: int) -> bool:
    for i in range(10000):
        g = random.randint(2, n - 1)
        if pow(g, n-1, n) != 1:
            return False
    return True


def Test_SSt(n: int) -> bool:
    for i in range(10000):
        a = random.randint(2, n - 1)
        g = ((n - 1) // 2)
        r = pow(a, g, n)

        if gcd(a, n) > 1:
            return False

        if r != 1 and r != n - 1:
            return False

        if r % n != sympy.jacobi_symbol(a, n) % n:
            return False

    return True


def Test_MR(n: int) -> bool:
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(10000):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def Tests(n: int) -> str:
    if Test_Ferma(n) == False: return f"{cl.RED}Число {cl.WHITE}{n} {cl.RED}составное (по тесту Ферма)"
    if Test_SSt(n) == False: return f"{cl.RED}Число {cl.WHITE}{n} {cl.RED}составное (по тесту Соловэя-Штрассена)"
    if Test_MR(n) == False: return f"{cl.RED}Число {cl.WHITE}{n} {cl.RED}составное (по тесту Миллера-Рабина)"
    return f"{cl.GREEN}Число {cl.WHITE}{n}{cl.GREEN} с большой вероятностью {cl.WHITE}{'простое'.upper()}"


num = int(sys.argv[1])

print(Tests(num))
