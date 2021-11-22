import random
import string

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
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m


# hold binary values

# hold key values
keyHolder = []





def repeat_key(length):
    keyString = ""
    for i in range(length):
        if i < 3:
            keyString += "0"
        else:
            keyString += str(random.randint(0, 1))
    return keyString


def encrypt_stream(plaintext):
    result = []
    key = []
    binary = []
    for i in plaintext:
        binary.append(toBinary(i))
    for x in range(len(binary)):
        temp = '.'.join(str(t) for t in binary[x])
        string = repeat_key(len(temp))
        key.append(string)
        #keyHolder.append(string)
        y = int(str(temp), 2) ^ int(string, 2)
        result.append(y)
    binary.clear()
    for z in result:
        binary.append(chr(z))
    return ''.join(binary)


def decrypt_stream(cipher, key):
    result = []
    original = []
    binary = []
    cipher = list(cipher)
    for x in range(len(cipher)):
        original.append(toBinary(cipher[x]))
        temp = '.'.join(str(t) for t in original[x])
        y = int(str(temp), 2) ^ int(str(key[x]), 2)
        result.append(y)

    for z in result:
        binary.append(chr(z))
    return ''.join(binary)


test = encrypt_stream("boe8")

#print(keyHolder)
#print(test)
#print(decrypt_stream(test, keyHolder))






def index_locator(char, cipherKeyMatrix):
    indexOfChar = []
    if char == "J":
        char = "I"
    for i, j in enumerate(cipherKeyMatrix):
        for k, l in enumerate(j):
            if char == l:
                indexOfChar.append(i)  # 1st dimension of 5X5 matrix
                indexOfChar.append(k)  # 2nd dimension of 5X5 matrix
                return indexOfChar


def encryptPlayfair(plaintext2, before_key):
    if all(chr.isalpha() for chr in plaintext2) and ' ' not in plaintext2:
        plaintext2 = plaintext2.upper()
        for s in range(0, len(plaintext2) + 1, 2):
            if s < len(plaintext2) - 1:
                if plaintext2[s] == plaintext2[s + 1]:
                    plaintext2 = plaintext2[:s + 1] + 'X' + plaintext2[s + 1:]
    else:
        return "Text can only have alphabetic letters"

    if 'J' in before_key or " " in before_key or 'j' in before_key:
        return "Key can't have J's or spaces for decryption"
    for i in before_key:
        if before_key.count(i) > 1 or before_key.isalpha() is False:
            return "Key cannot have repeating characters or non-alphabetic characters"

    # append X if the total letters are odd, to make plaintext even
    if len(plaintext2) % 2 != 0:
        plaintext2 = plaintext2[:] + 'X'

    matrix_5x5 = [[0 for i in range(5)] for j in range(5)]
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    """
    Fill in the missing alphabets
    """
    before_key = list(before_key.upper())
    index = 0
    new_key = []
    for i in range(0, 26 + len(before_key)):
        if i < len(before_key):
            new_key.append(before_key[i])
        elif abc[index] in new_key or abc[index] == "J":
            index += 1
        else:
            new_key.append(abc[index])
            index += 1
    """
    Fill matrix_5x5 with new_key
    """
    index = 0
    for i in range(0, 5):
        for j in range(0, 5):
            matrix_5x5[i][j] = new_key[index]
            index += 1
    cipher = []
    i = 0
    # print(index_locator("J", matrix_5x5))
    firstVal = False
    secondVal = False

    while i < len(plaintext2):
        # 2.1 calculate two grouped characters indexes from keyMatrix
        n1 = index_locator(plaintext2[i], matrix_5x5)
        n2 = index_locator(plaintext2[i + 1], matrix_5x5)
        if plaintext2[i] == "J":
            firstVal = True
        elif plaintext2[i + 1] == "J":
            secondVal = True

        if int(n1[1]) == int(n2[1]):
            i1 = (n1[0] + 1) % 5
            j1 = n1[1]

            i2 = (n2[0] + 1) % 5
            j2 = n2[1]

            if firstVal == True:
                cipher.append("J")
                cipher.append(matrix_5x5[i2][j2])
                firstVal = False

            elif secondVal == True:
                cipher.append(matrix_5x5[i1][j1])
                cipher.append("J")
                secondVal = False

            else:
                cipher.append(matrix_5x5[i1][j1])
                cipher.append(matrix_5x5[i2][j2])

        # same row
        elif int(n1[0]) == int(n2[0]):
            i1 = n1[0]
            j1 = (n1[1] + 1) % 5

            i2 = n2[0]
            j2 = (n2[1] + 1) % 5

            if firstVal == True:
                cipher.append("J")
                cipher.append(matrix_5x5[i2][j2])
                firstVal = False

            elif secondVal == True:
                cipher.append(matrix_5x5[i1][j1])
                cipher.append("J")
                secondVal = False

            else:
                cipher.append(matrix_5x5[i1][j1])
                cipher.append(matrix_5x5[i2][j2])

        # if making rectangle then

        else:
            i1 = n1[0]
            j1 = n1[1]

            i2 = n2[0]
            j2 = n2[1]
            if firstVal == True:
                cipher.append("J")
                cipher.append(matrix_5x5[i2][j1])
                firstVal = False

            elif secondVal == True:
                cipher.append(matrix_5x5[i1][j2])
                cipher.append("J")
                secondVal = False

            else:
                cipher.append(matrix_5x5[i1][j2])
                cipher.append(matrix_5x5[i2][j1])
        i += 2
    cipher = ''.join(cipher)
    return cipher


def decrypt_playfair(cipherText, keyword):
    if all(chr.isalpha() for chr in
           cipherText) and ' ' not in cipherText and 'J' not in cipherText and 'j' not in cipherText:
        cipherText = cipherText.upper()
    else:
        return "Ciphertext can only have alphabetic letters and no J's"

    for i in range(len(cipherText) - 1):
        if cipherText[i] == cipherText[i + 1]:
            return "Ciphertext cannot have duplicate letters next to each other"
    if 'J' in keyword or " " in keyword or 'j' in keyword:
        return "Key can't have J's or spaces for decryption"
    for i in keyword:
        if keyword.count(i) > 1 or keyword.isalpha() is False:
            return "Key cannot have repeating characters or non-alphabetic characters"
    matrix_5x5 = [[0 for i in range(5)] for j in range(5)]
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    """
    Fill in the missing alphabets
    """
    before_key = keyword.upper()
    before_key = list(before_key)
    index = 0
    new_key = []
    for i in range(0, 26 + len(before_key)):
        if i < len(before_key):
            new_key.append(before_key[i])
        elif abc[index] in new_key or abc[index] == "J":
            index += 1
        else:
            new_key.append(abc[index])
            index += 1
    """
    Fill matrix_5x5 with new_key
    """
    index = 0
    for i in range(0, 5):
        for j in range(0, 5):
            matrix_5x5[i][j] = new_key[index]
            index += 1

    cipher = []
    plaintext2 = cipherText

    i = 0
    while i < len(plaintext2):
        # 2.1 calculate two grouped characters indexes from keyMatrix
        n1 = index_locator(plaintext2[i], matrix_5x5)
        n2 = index_locator(plaintext2[i + 1], matrix_5x5)

        # same column
        if int(n1[1]) == int(n2[1]):
            i1 = (n1[0] - 1) % 5
            j1 = n1[1]

            i2 = (n2[0] - 1) % 5
            j2 = n2[1]

            cipher.append(matrix_5x5[i1][j1])
            cipher.append(matrix_5x5[i2][j2])

        # same row
        elif int(n1[0]) == int(n2[0]):
            i1 = n1[0]
            j1 = (n1[1] - 1) % 5

            i2 = n2[0]
            j2 = (n2[1] - 1) % 5

            cipher.append(matrix_5x5[i1][j1])
            cipher.append(matrix_5x5[i2][j2])

        # if making rectangle then
        else:
            i1 = n1[0]
            j1 = n1[1]

            i2 = n2[0]
            j2 = n2[1]

            cipher.append(matrix_5x5[i1][j2])
            cipher.append(matrix_5x5[i2][j1])
        i += 2

    cipher = ''.join(cipher)
    print(matrix_5x5)
    return cipher
# cipher = initialize_matrix("SECRETMESSAGE", "keyword")
# print(cipher)
# print(decrypt_playfair("NORDKUNKQZPCNDAA", "keyword"))
# print(decrypt_playfair("LW", (initialize_matrix("JO", "keyword"))))
