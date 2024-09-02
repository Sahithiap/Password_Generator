from tkinter import *
import random, string
import pyperclip

# Create the main application window
root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("PYTHON PROJECT - PASSWORD GENERATOR")

# Title labels
Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(root, text='Python', font='arial 15 bold').pack(side=BOTTOM)

# Password length label and Spinbox
pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

# StringVar to store the generated password
pass_str = StringVar()

# Function to generate password
def Generator():
    password = []
    
    # Ensuring at least one character from each type (Uppercase, Lowercase, Digits, Punctuation)
    if pass_len.get() >= 4:
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))

        # Fill the rest with random choices until the specified length
        for _ in range(pass_len.get() - 4):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
        
        # Shuffle to ensure randomness
        random.shuffle(password)
    else:
        # If length is less than 4, just fill the required length with random choices
        for _ in range(pass_len.get()):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
    
    # Convert list to string and set it to the variable
    pass_str.set(''.join(password))

# Function to copy password to clipboard
def Copy_password():
    pyperclip.copy(pass_str.get())

# Buttons and Entry fields
Button(root, text='GENERATE PASSWORD', command=Generator).pack(pady=5)
Entry(root, textvariable=pass_str).pack()
Button(root, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=5)

root.mainloop()
