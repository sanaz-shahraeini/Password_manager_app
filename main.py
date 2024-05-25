from tkinter import *
import random


def create_password():
    selected_numbers = []
    selected_letters = []
    selected_signs = []

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
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
    result_string = ''.join(result_list)
    password_label.config(text=result_string, fg=blue)

    # save to file
    site = site_address_entry.get()
    generated_pass = password_label.cget("text")
    data_file = open("information.txt", "a")
    data_file.write("site_address :" + site + "\n")
    data_file.write("password :" + generated_pass + "\n")
    return data_file





# UI Part :----------------

window = Tk()
window.geometry("270x520")  # Set window size
window.title("Password Manager App")  # Set window title
window.config(bg="white")
window.resizable(0, 0)
window.iconbitmap("pass.ico")

blue = "midnight blue"
font_name = "Arial"
# widgets
canvas = Canvas(width=200, height=224)
my_img = PhotoImage(file="passimg.png")
canvas.create_image(100, 112, image=my_img)
canvas.grid(row=0, column=0)

site_address_label = Label(window, text="Enter site address :", bg="white", font=(font_name, 15))
site_address_entry = Entry(window, width=40, bd=5)
create_pass_button = Button(window, text="Create Password", fg="white", bg=blue, width=12, font=(font_name, 10),
                            command=create_password)
retive_pass_button = Button(window, text="Retive Password", fg="white", bg=blue, width=12, font=(font_name, 10))
password_label = Label(window, width=30, bg="gray92", height="2", text="password...", fg="white")
exit_button = Button(window, text="Exit App", fg="white", bg=blue, width=8, font=(font_name, 10), command=window.quit)

# layout
site_address_label.grid(row=1, column=0, padx=15, pady=25)
site_address_entry.grid(row=2, column=0, padx=10)
create_pass_button.grid(row=3, column=0, pady=15)
retive_pass_button.grid(row=4, column=0, pady=7)
password_label.grid(row=6, column=0)
exit_button.grid(column=0, row=5, pady=7)

window.mainloop()

