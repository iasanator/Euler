def is_pal(test):

    flag = True

    for i in range(1, int((len(test)) / 2) + 1):
        if test[i - 1] != test[len(test) - i]:
            flag = False
    return flag

sum = 0

for num in range(0, 1000000):
    if is_pal(str(num)) and is_pal(str(bin(num).split('b')[1])):
        print('FOUND: ' + str(num))
        sum += num

print(sum)