import random


def Convert_To_String(myList):
    text = ''
    for i in myList:
        text = text + str(i) + ""
    return text


Selected_numbers = []
Selected_letters = []
Selected_signs = []
Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Letters = ["a", "b", "c", "d", " e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
           "r", "s", "t", "u", "v", "w", "x", "y", "m", "z",
           "A", "B", "C", "D", " E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
           "R", "S", "T", "U", "V", "W", "X", "Y", "M", "Z",
           ]
signs = ["~", "!", "#", "$", "%", "^", "&", "*", "(", ")", "_", "|"]
for i in range(3):
    Num = random.choice(Numbers)
    Selected_numbers.append(Num)
    Letter = random.choice(Letters)
    Selected_letters.append(Letter)
    Sign = random.choice(signs)
    Selected_signs.append(Sign)

result_list = Selected_letters + Selected_signs + Selected_numbers
random.shuffle(result_list)
print(Convert_To_String(result_list))