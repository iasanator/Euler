for a in range(1, 1001):
    for b in range(a + 1, 1001):
        if ((a ** 2 + b ** 2) == (1000 - a - b) ** 2)\
                and ((a + b + (1000 - a - b)) == 1000):
            print(a)
            print(b)
            print(1000 - a - b)
            exit()