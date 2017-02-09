fibs = [0, 1, 1]
def fib(n):
    if len(fibs) <= n:
        fibs.append(fib(n - 1) + fib(n - 2))
    return fibs[n]


def is_pandigital(str):
    digits = []
    for digit in str:
        if digit not in digits and digit != '0':
            digits.append(digit)
    return len(digits) == 9

k = 1
while(True):
    num = fib(k)
    if k % 10000 == 0: print(k)
    if is_pandigital(str(num % 1000000000)) and is_pandigital(str(num)[:9]):
        print(k)
        exit()
    k += 1
