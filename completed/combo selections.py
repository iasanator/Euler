fact_vals = {}

def fact(n):
    if n in fact_vals.keys():
        return fact_vals[n]
    else:
        if n == 0:
            fact_vals[n] = 1
        else:
            fact_vals[n] = n * fact(n - 1)
    return fact_vals[n]

def choose(n, r):
    return int(fact(n) / (fact(r) * fact(n - r)))

import time
start_time = time.time()

sum = 0
for n in range(1, 101):
    for r in range(0, n + 1):
        if choose(n, r) > 1000000:
            sum += 1

print(int((time.time() - start_time) * 1000), 'milliseconds')
print(sum)
