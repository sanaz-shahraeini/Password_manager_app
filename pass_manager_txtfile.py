from tkinter import *
import random
from tkinter import messagebox

file_name = "information.txt"


def recovery_password():
    try:
        site = site_address_entry.get()
        if site:
            with open("information.txt", "r") as file:
                for line in file:
                    parts_list = line.strip().split(" -> ")
                if parts_list[0] == site:
                    messagebox.showwarning("warning", parts_list[1])
                    site_address_entry.delete(0, END)
                else:
                    messagebox.showwarning("Warning", "Not Found!.")
                    site_address_entry.delete(0, END)
        else:
          messagebox.showwarning("warning", "pls enter site address")

    except:
        messagebox.showwarning("warning", "database is empty")


def save_to_file():
    site = site_address_entry.get()
    generated_pass = password_label.cget("text")
    if site:
        if generated_pass:
            with open(file_name, "a") as file:
                file.write(f"{site} -> {generated_pass} \n")
            messagebox.showwarning("Notifications", "The password has been successfully saved.")
            site_address_entry.delete(0, END)
            password_label.config(text="")
        else:
            messagebox.showwarning("warning", "before save need to create password")
    else:
        messagebox.showwarning("warning", "pls enter site address")


def create_password():
    selected_numbers = []
    selected_letters = []
    selected_signs = []
    site = site_address_entry.get()
    generated_pass = password_label.cget("text")

    try:
        if site:
            with open(file_name, "r") as file:
                if site in file.read():
                    messagebox.showwarning("Warning", "site already saved in the file!")
                    site_address_entry.delete(0, END)
                else:
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
        else:
            messagebox.showwarning("Warning", "please enter site address!.")

    except FileNotFoundError:
        with open(file_name, "a") as file:
            file.write(f"{site} -> {result_string} \n")


# UI Part :----------------

window = Tk()
window.geometry("270x550")  # Set window size
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
create_pass_button = Button(window, text="Create Password", fg="white", bg=blue, width=12,
                            font=(font_name, 10), command=create_password)
retrieve_pass_button = Button(window, text="Retrieve Password", fg="white", bg=blue, width=14, font=(font_name, 10),
                              command=recovery_password)
password_label = Label(window, width=30, bg="gray92", height="2", fg="white")
exit_button = Button(window, text="Exit App", fg="white", bg=blue, width=8, font=(font_name, 10), command=window.quit)
save_button = Button(window, text="Save password", fg="white", bg=blue, width=12, font=(font_name, 10),
                     command=save_to_file)

# layout
site_address_label.grid(row=1, column=0, padx=15, pady=25)
site_address_entry.grid(row=2, column=0, padx=10)
create_pass_button.grid(row=3, column=0, pady=15)
retrieve_pass_button.grid(row=5, column=0, pady=7)
password_label.grid(row=7, column=0)
exit_button.grid(column=0, row=6, pady=7)
save_button.grid(column=0, row=4, pady=7)

window.mainloop()
