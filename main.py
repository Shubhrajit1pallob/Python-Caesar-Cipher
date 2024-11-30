import string
from operator import index
from turtledemo.chaos import jumpto
from uu import encode

lowercase_alphabets = list(string.ascii_lowercase)

# Function to encrypt the message
def encrypt(msg, shift):
    encoded_msg = ""
    for ch in msg:
        if ch in lowercase_alphabets:
            # print("the control is reaching here!")
            index_of_ch = lowercase_alphabets.index(ch)
            index_shift = index_of_ch+shift
            index_shift %= len(lowercase_alphabets)
            encoded_msg += lowercase_alphabets[index_shift]
            # print(encoded_msg)
        else:
            encoded_msg += ch
    # print("The control is reaching here")
    print(encoded_msg)


def decrypt(msg, shift):
    decoded_msg = ""
    for ch in msg:
        if ch in lowercase_alphabets:
            index_of_ch = lowercase_alphabets.index(ch)
            index_shift = index_of_ch-shift
            if index_shift<0:
                index_shift = 26+index_shift
            decoded_msg += lowercase_alphabets[index_shift]
        else:
            decoded_msg += ch
    print(decoded_msg)

# Take input from the user
while True:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
    text_msg = input("Type your message: \n").lower()
    shift = int(input("Enter the shift number: \n"))

    if direction=="encode":
        encrypt(text_msg, shift)
    if direction =="decode":
        decrypt(text_msg, shift)

    next_dir = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if next_dir == "no":
        print("Goodbye!")
        break
