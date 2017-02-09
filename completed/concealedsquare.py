import math

k = math.sqrt(1000000000000000000)
n = math.sqrt(1929394959697989900)
print(k, n)

def is_ans(num):
    s = str(num)
    if s[0] == '1' and s[2] == '2' and s[4] == '3' and s[6] == '4' and s[8] == '5' and s[10] == '6' and s[12] == '7' and s[14] == '8' and s[16] == '9' and s[18] == '0':
        return True
    return False

i = int(k)
while(True):
    if (i % 100 == 30 or i % 100 == 70) and is_ans(i**2):
        print(i, i**2)
        exit()
    i += 10
    if i > n:
        print('failed')
        exit()