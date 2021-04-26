# import required module
from cryptography.fernet import Fernet
from tkinter import filedialog
from tkinter import *
import os
#######################################################
root = Tk()
folder_path = StringVar()
root.title('lucasrasmuss585')
#######################################################
def selectDirforDecription(path):
    # Change the directory
    os.chdir(path)
    # Read text File
    # iterate through all file
    tryDone = 0
    key = 0
    with open(path + '/filekey.key', 'rb') as filekey:
        key = filekey.read()
    # using the generated key
    fernet = Fernet(key)
    for filename in os.listdir():
        # Check whether file is in text format or not
        if filename.endswith(".txt"):
            # opening the original file to encrypt
            with open(filename, 'rb') as file:
                original = file.read()
            # encrypting the file
            encrypted = fernet.decrypt(original)
            # opening the file in write mode and
            # writing the encrypted data
            with open(filename, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            # call read text file function
        else:
            tryDone += 1
    print("Encripted")
    lbl1['text'] = 'Done'
def selectDirforEncription(path):
    # Change the directory
    os.chdir(path)
    # Read text File
    # iterate through all file
    tryDone = 0
    key = Fernet.generate_key()
    with open(path + '/filekey.key', 'wb') as filekey:
        filekey.write(key)
    with open(path + '/filekey.key', 'rb') as filekey:
        key = filekey.read()
    # using the generated key
    fernet = Fernet(key)
    for filename in os.listdir():
        # Check whether file is in text format or not
        if filename.endswith(".txt"):
            # opening the original file to encrypt
            with open(filename, 'rb') as file:
                original = file.read()
            # encrypting the file
            encrypted = fernet.encrypt(original)
            # opening the file in write mode and
            # writing the encrypted data
            with open(filename, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            # call read text file function
        else:
            tryDone += 1
    print("Encripted")
    lbl1['text'] = 'Done'
def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    lbl1['text'] = ''
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    selectDirforEncription(filename)
def browse_button_two():
    # Allow user to select a directory and store it in global var
    # called folder_path
    lbl1['text'] = ''
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    selectDirforDecription(filename)



Label(text="lucasrasmuss585", width = 20, height = 1).pack()
# lbl1.grid(row=3, column=3)

lbl2 = Label(text="Text file Encriptor", width = 20, height = 3)
# lbl1.grid(row=3, column=3)
lbl2.pack()

button2 = Button(text="Encrypt", command=browse_button, fg='black', bg='skyblue')
# button2.grid(row=1, column=3)
button2.pack()
button2 = Button(text="Decrypt", command=browse_button_two, fg='black', bg='skyblue')
# button2.grid(row=1, column=3)
button2.pack()

lbl1 = Label(text="waiting")
# lbl1.grid(row=3, column=3)
lbl1.pack()

mainloop()