#Parse Word File
words = open('trianglenums.txt', 'r').read().translate({ord(c): None for c in '"'}).split(',')

#find Max Length
max_length = 0
for word in words:
    word_length = len(word)
    if word_length > max_length:
        max_length = word_length

#Define letter --> number
def enum_letter(letter):
    data = ord(letter)
    if data < 97:
        return data - 64
    return data - 96

#Generate triangle number table with all needed triangle numbers
def get_nth_triangle_num(n):
    return int(0.5 * n * (n + 1))

max_sum = max_length * enum_letter('z')

triangle_nums = [1]

while (triangle_nums[len(triangle_nums) - 1] < max_sum):
    triangle_nums.append(get_nth_triangle_num(len(triangle_nums) + 1))

#Define word --> number
def enum_word(word):
    sum = 0
    for letter in word:
        sum += enum_letter(letter)
    return sum

#Deterine if each word is a triangle word
triangle_word_count = 0
for word in words:
    if enum_word(word) in triangle_nums:
        triangle_word_count += 1

print(triangle_word_count)