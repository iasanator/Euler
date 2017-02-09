# from bisect import bisect
#
# one_chain = [1]
# eightynine_chain = [4, 16, 20, 37, 42, 89, 145]
#
# def square_digits(num):
#     sum = 0
#     for digit in str(num):
#          sum += int(digit)**2
#     return sum
#
# def sorted_contains(list, entry):
#     return list[bisect(list, entry) - 1] == entry
#
# for num in range(1, 10000000):
#
#     if num % 10000 == 0:
#         print(num)
#         print(num / 10000000 * 100)
#
#     square_chain = [num]
#     last_link = square_chain[len(square_chain) - 1]
#
#     while (not sorted_contains(one_chain, last_link)) and (not sorted_contains(eightynine_chain, last_link)):
#         square_chain.append(square_digits(last_link))
#         last_link = square_chain[len(square_chain) - 1]
#
#     square_chain.pop()
#
#     if (last_link in one_chain):
#         for link in square_chain:
#             one_chain.insert(bisect(one_chain, link), link)
#     else:
#         for link in square_chain:
#             eightynine_chain.insert(bisect(eightynine_chain, link), link)
#
# print(len(eightynine_chain))
# print(len(one_chain))

one_chain = []
eightynine_chain = []

digit_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def square_digits(num):
    sum = 0
    for digit in str(num):
         sum += digit_squares[int(digit)]
    return sum

for num in range(1, 10000000):

    if num % 10000 == 0:
        print(num)
        print(num / 10000000 * 100)

    square_chain = [num]
    last_link = square_chain[len(square_chain) - 1]

    while last_link != 1 and last_link != 89:
        square_chain.append(square_digits(last_link))
        last_link = square_chain[len(square_chain) - 1]

    square_chain.pop()

    if last_link == 1:
        one_chain.append(num)
    else:
        eightynine_chain.append(num)

print(len(eightynine_chain))
print(len(one_chain))