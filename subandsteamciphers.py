import random

"""
while True:
    try:
        mode = int(input("Press 1 for Encryption \n \t  2 for Decryption \n \t  3 for Quit\nEnter: "))
    except ValueError:
        print("Sorry, please enter a number")
        # better try again... Return to the start of the loop
        continue
    if mode < 1 or mode > 3:
        print("Please enter a valid number")
        # age was successfully parsed!
        # we're ready to exit the loop.
    else:
        break
while True:
    try:
        cipher = int(input("Press 4 for Stream Cipher \n \t  5 for Playfair Cipher\nEnter: "))
    except ValueError:
        print("Sorry, please enter a number")
        # better try again... Return to the start of the loop
        continue
    if cipher < 4 or cipher > 5:
        print("Please enter a valid number")
        # age was successfully parsed!
        # we're ready to exit the loop.
    else:
        break
"""
# change ascii character to binary
def toBinary(a):
  l,m = [],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

# hold binary values
binary = []
# hold key values
key = []

result = []


def repeat_key(length):
    keyString = ""
    for i in range(length):
        if i < 3:
            keyString += "0"
        else:
            keyString += str(random.randint(0, 1))
    return keyString

def encrypt_stream(plaintext):
    for i in plaintext:
        binary.append(toBinary(i))
    for x in range(len(binary)):
        temp = '.'.join(str(t) for t in binary[x])
        string = repeat_key(len(temp))
        key.append(string)
        y = int(str(temp), 2) ^ int(string, 2)
        result.append(y)
        print(y)
    binary.clear()
    for z in result:
        binary.append(chr(z))
    return binary
original = []

def decrypt_stream(cipher, key):
    result.clear()
    for x in range(len(cipher)):
        original.append(toBinary(cipher[x]))
        temp = '.'.join(str(t) for t in original[x])
        y = int(str(temp), 2) ^ int(str(key[x]), 2)
        result.append(y)
    binary.clear()
    for z in result:
        binary.append(chr(z))
    return binary

#test = encrypt_stream("boi8")
#print(test)
#print(decrypt_stream(test, key))
