def factorial(n, result=1):
    if n == 1:
        return result
    return lambda: factorial(n-1, result*n)


def fibbonaci_rec(n, i=1, a=0, b=1):
    if n == i:
        return a
    return lambda: fibbonaci_rec(n, i+1, b, b+a)


def trampoline(f, n):
    acc = f(n)
    while '__call__' in dir(acc):
        acc = acc()
    return acc


print(trampoline(fibbonaci_rec, 500))
# print(trampoline(factorial, 1500))
