# import the necessary modules
import tkinter
import random

# generate password using random module
def generate_password():
    global password
    character_inputs = "abc-defg-hijk-lmno-pqrs-tuvw-xyz-123-456-7890-ABC-DEF-GHI-JKL-MNO-PQR-STU-VWX-YZ-!@#-$%^-&*-?:"
    password_length = 12
    password = "".join(random.sample(character_inputs, password_length))
    password_label.config(text="Generated Password: " + password)

# function to copy password to clipboard
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password)

# function to exit the program
def exit_program():
    root.destroy()

# create tkinter window
root = tkinter.Tk()
root.title("Password Generator")

# create label for password
password_label = tkinter.Label(root, text="Click 'Generate Password' to create a new password.")
password_label.pack(pady=10)

# create button to generate password
generate_button = tkinter.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

# create button to copy password to clipboard
copy_button = tkinter.Button(root, text="Copy to Clipboard", command=copy_password)
copy_button.pack(pady=5)

# create button to exit program
exit_button = tkinter.Button(root, text="Exit", command=exit_program)
exit_button.pack(pady=5)

# run the tkinter loop
root.mainloop()
