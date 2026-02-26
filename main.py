import random
from tkinter import *
from tkinter import filedialog, ttk

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+{}|:<>?~`-=[];',./"
numbers = "1234567890"


def gen_password():
    output.delete(1.0, END)
    chars = ""
    if has_alphabet.get():
        chars += alphabet
    if has_symbol.get():
        chars += symbols
    if has_number.get():
        chars += numbers

    if not chars:
        output.insert(END, "Select has alphabet, symbol or  number!")
        return

    if not length_entry.get():
        output.insert(END, "Type password length!")
        return

    for i in range(int(length_entry.get())):
        if chars:
            output.insert(END, random.choice(chars))
        else:
            output.insert(END, "Please select at least one checkbox")

window = Tk()
window.geometry("280x320")
window.attributes("-toolwindow", True)
window.resizable(False, False)
window.title("")

has_alphabet = IntVar(value=0)
has_symbol = IntVar(value=0)
has_number = IntVar(value=0)

label = Label(window, text="Password Generator", font=("Arial", 20))
label.place(x=10, y=0)

output = Text(window, height=10, width=32)
output.place(x=10, y=50)

gen_button = ttk.Button(window, text="Generate Password", command=gen_password)
gen_button.place(x=10, y=220)


has_alphabet_checkbox = ttk.Checkbutton(window, text="Has Alphabet", variable=has_alphabet)
has_alphabet_checkbox.place(x=10, y=250)

has_symbols_checkbox = ttk.Checkbutton(window, text="Has Symbol", variable=has_symbol)
has_symbols_checkbox.place(x=10, y=270)

has_number_checkbox = ttk.Checkbutton(window, text="Has Number", variable=has_number)
has_number_checkbox.place(x=10, y=290)


length_label = Label(window, text="Length:")
length_label.place(x=140, y=222)

length_entry = ttk.Entry(window, width=10)
length_entry.place(x=190, y=222)

window.mainloop()