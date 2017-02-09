def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

from collections import deque

def generate_rotations(str, func):
    rotations = set()
    for i in range(0, len(str)):
        rotations.add(func(str[i:] + str[:i]))
    return list(rotations)

def contains_even(num):
    numstr = str(num)
    for digit in numstr:
        if int(digit) % 2 == 0 or int(digit) == 5:
            return True
    return False

circular_primes = set()
circular_primes.add(2)
circular_primes.add(5)

for num in range(3, 1000000):

    if contains_even(num): continue

    if num not in circular_primes:
        rotations = generate_rotations(str(num), lambda x : int(x))

        flag = True
        for rotation in rotations:
            if not is_prime(rotation):
                flag = False
                break
        if flag:
            for rotation in rotations:
                circular_primes.add(rotation)

print(circular_primes)
print(len(circular_primes))
