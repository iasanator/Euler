def is_bouncy(num):
    if not (is_decreasing(num) or is_increaing(num)):
        return True
    return False

def is_increaing(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if int(num_str[i]) < int(num_str[i - 1]):
            return False
    return True

def is_decreasing(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        if int(num_str[i]) > int(num_str[i - 1]):
            return False
    return True

total_bouncy = 0
total_not_bouncy = 100

index = 100

while (total_bouncy / index) < 0.99:
    index += 1
    if is_bouncy(index):
        total_bouncy += 1
    else:
        total_not_bouncy += 1

print(index)