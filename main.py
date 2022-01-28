from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list_letters = [choice(letters) for _ in range(nr_letters)]
    password_list_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_list = password_list_letters + password_list_numbers + password_list_symbols

    shuffle(password_list)
    password_gen = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password_gen)
    pyperclip.copy(password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    data_website_title = entry_website_title.get()
    data_website_url = entry_website_url.get()
    data_username = entry_username.get()
    data_password = entry_password.get()

    new_data = {
        data_website_title: {
            "Url": data_website_url,
            "Username": data_username,
            "Password": data_password,
        }
    }

    if len(data_website_title) == 0 or len(data_username) == 0 or len(data_password) == 0 or len(data_website_url) == 0:
        messagebox.showwarning(title="Error - Empty fields", message="Please fill out all required fields!")
    else:
        confirm = messagebox.askokcancel(title=data_website_title, message=f"These are the details entered: \n\n"
                                                                           f"Username: {data_website_url}\n"
                                                                           f"Username: {data_username}\n"
                                                                           f"Password: {data_password}\n\n"
                                                                           f"Do you want to save these information?")
        if confirm:
            try:
                with open("data.json", "r") as f:
                    db = json.load(f)
                    db.update(new_data)

                with open("data.json", "w") as f:
                    json.dump(db, f, indent=4)

            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)

            entry_website_url.delete(0, END)
            entry_website_title.delete(0, END)
            entry_website_url.insert(0, string="https://www.")
            entry_username.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_db():
    search_title = entry_website_title.get().title()

    with open("data.json", "r") as f:
        data = json.load(f)

    if search_title in data:
        print("drin")
        messagebox.showinfo(title="Password found!", message=f"Your infos:\n\n"
                                                             f"Website Title: '{search_title}'\n"
                                                             f"Website URL: '{data[search_title]['Url']}'\n"
                                                             f"Username: '{data[search_title]['Username']}'\n"
                                                             f"Password: '{data[search_title]['Password']}'\n\n"
                                                             f"Copied your password to the clipboard.")
        pyperclip.copy(data[search_title]['Password'])
    else:
        messagebox.showinfo("Password not found!", message=f"There is no entry with the title: {search_title}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Jörg - Password Manager")
window.config(padx=30, pady=30, background="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# LABELS
website_title = Label(text="Website Title: ", background="white")
website_url = Label(text="Website URL: ", background="white")
username = Label(text="Username: ", background="white")
password = Label(text="Password: ", background="white")

website_title.grid(column=0, row=1, sticky="w")
website_url.grid(column=0, row=2, sticky="w")
username.grid(column=0, row=3, sticky="w")
password.grid(column=0, row=4, sticky="w")

# INPUTS
entry_website_title = Entry()
entry_website_title.focus()
entry_website_title.grid(column=1, row=1, columnspan=2, sticky="ew")

entry_website_url = Entry()
entry_website_url.insert(END, string="https://www.")
entry_website_url.focus()
entry_website_url.grid(column=1, row=2, columnspan=2, sticky="ew")

entry_username = Entry()
entry_username.grid(column=1, row=3, columnspan=2, sticky="ew")

entry_password = Entry()
entry_password.grid(column=1, row=4, sticky="ew")

# BUTTONS
generate_pass = Button(text="Generate", command=generate)
generate_pass.grid(column=2, row=4, sticky="ew")

add = Button(text="Add", command=add_pass)
add.grid(column=1, row=5, columnspan=2, sticky="ew")

search = Button(text="Search", command=search_db)
search.grid(column=2, row=1, sticky="ew")

window.mainloop()
