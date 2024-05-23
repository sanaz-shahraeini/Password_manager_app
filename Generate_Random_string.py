import random


def convert_to_string(myList):
    text = ''
    for i in myList:
        text = text + str(i)
    return text


selected_numbers = []
selected_letters = []
selected_signs = []

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
           "r", "s", "t", "u", "v", "w", "x", "y", "m", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
           "R", "S", "T", "U", "V", "W", "X", "Y", "M", "Z",
           ]
signs = ["~", "!", "#", "$", "%", "^", "&", "*", "(", ")", "_", "|"]
for i in range(5):
    num = random.choice(numbers)
    selected_numbers.append(num)
    letter = random.choice(letters)
    selected_letters.append(letter)
    sign = random.choice(signs)
    selected_signs.append(sign)

result_list = selected_letters + selected_signs + selected_numbers
result_list.pop()
random.shuffle(result_list)
print(convert_to_string(result_list))