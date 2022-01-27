from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list_letters = [choice(letters) for i in range(nr_letters)]
    password_list_numbers = [choice(numbers) for i in range(nr_numbers)]
    password_list_symbols = [choice(symbols) for i in range(nr_symbols)]
    password_list = password_list_letters + password_list_numbers + password_list_symbols

    shuffle(password_list)

    password_gen = ""
    for char in password_list:
        password_gen += char

    entry_password.delete(0, END)
    entry_password.insert(0, password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    data_website = entry_website.get()
    data_username = entry_username.get()
    data_password = entry_password.get()

    if len(data_website) == 0 or len(data_username) == 0 or len(data_password) == 0:
        messagebox.showwarning(title="Error - Empty fields", message="Please fill out all required fields!")
    else:
        confirm = messagebox.askokcancel(title=data_website, message=f"These are the details entered: \n\n"
                                                                     f"Username: {data_username}\n"
                                                                     f"Password: {data_password}\n\n"
                                                                     f"Do you want to save these information?")
        if confirm:
            with open("data.txt", "a") as f:
                f.write(f"{data_website}, {data_username}, {data_password}\n")

            entry_website.delete(0, END)
            entry_website.insert(0, string="https://www.")
            entry_username.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Sinclair - Password Manager")
window.config(padx=30, pady=30, background="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# LABELS
website = Label(text="Website: ", background="white")
username = Label(text="Username: ", background="white")
password = Label(text="Password: ", background="white")
website.grid(column=0, row=1, sticky="w")
username.grid(column=0, row=2, sticky="w")
password.grid(column=0, row=3, sticky="w")

# INPUTS
entry_website = Entry()
entry_website.insert(END, string="https://www.")
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2, sticky="ew")

entry_username = Entry()
entry_username.grid(column=1, row=2, columnspan=2, sticky="ew")

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="ew")

generate_pass = Button(text="Generate Password", command=generate)
generate_pass.grid(column=2, row=3, sticky="ew")

# calls action() when pressed
add = Button(text="Add", command=add_pass, width=34)
add.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()
