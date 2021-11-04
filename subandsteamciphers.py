import random

while True:
    try:
        mode = input("Press 1 for Encryption \n \t  2 for Decryption \n \t  3 for Quit\nEnter: ")
    except ValueError:
        print("Sorry, please enter a number")
        #better try again... Return to the start of the loop
        continue
    if input < 1 or input > 3:
        print("Please enter a valid number")
        #age was successfully parsed!
        #we're ready to exit the loop.
    else:
        break
while True:
    try:
        cipher = input("Press 4 for Stream Cipher \n \t  5 for Playfair Cipher\nEnter: ")
    except ValueError:
        print("Sorry, please enter a number")
        #better try again... Return to the start of the loop
        continue
    if input < 4 or input > 5:
        print("Please enter a valid number")
        #age was successfully parsed!
        #we're ready to exit the loop.
    else:
        break

