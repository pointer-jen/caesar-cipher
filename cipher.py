# Write a Python program that encrypts text given by the user. The program should ask the user for a plain text sentence and print the encrypted text. The text should be encrypted using a caesar cipher with a right shift of 5.
abc = "abcdefghijklmnopqrstuvwxyz"

shift = 5
plain_text = input("Please enter the sentence to encrypt: ")
plain_text = plain_text.lower()

shifted_text = ""

for char in plain_text:
    if char in abc:
        index = abc.find(char)
        index = (index + shift) % 26
        char = abc[index]
    shifted_text += char

print(shifted_text)
