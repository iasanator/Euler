import math

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = []
for num in range(2, 190):
    if is_prime(num):
        primes.append(num)

product = 1
for num in primes:
        product = product * num

def get_sublist(sub, list):
    sublist = []
    for i in range(0, 42):
        if sub[i] == '1':
            sublist.append(list[i])
    return sublist

def format_sub(num):
    short = str(bin(num))[2:]
    zeroes_to_add = 42 - len(short)
    zeroes = ""
    for i in range(0, zeroes_to_add):
        zeroes += "0"
    return zeroes + short

divisors = []
for combo in range(10, 2 ** 42):
    if combo % 100000 == 0: print(combo)
    prod = 1
    for number in get_sublist(format_sub(combo), primes):
        prod = prod * number
    divisors.append(prod)

square_root = int(math.sqrt(product))
distance = -1
psr = 0
for divisor in divisors:
    if distance == -1:
        psr, distance = divisor, square_root - divisor
    else:
        if product < square_root and square_root - divisor < distance:
            psr, distance = divisor, square_root - divisor

print(psr)