import random
import math

generatedPlainText = ""
generatedCipherText = ""
generatedKey = ""

## TRANSPOSITION START
def encryptTransposition(plaintext):
    global generatedCipherText
    global generatedKey
    plaintext = plaintext.upper()
    possibleKeyLengths = range(2, 10)
    useKeyLength = random.choice(possibleKeyLengths)
    ciphertext = [""] * useKeyLength
    for col in range(useKeyLength):
        curr = col
        while curr < len(plaintext):
            ciphertext[col] += plaintext[curr]
            curr += useKeyLength
    
    generatedCipherText = "".join(ciphertext)
    generatedKey = useKeyLength

def decryptTransposition(ciphertext, key):
    global generatedPlainText
    col = math.ceil(len(ciphertext)/key)
    col = int(col)
    row = key
    unoccupied = (row * col) - len(ciphertext)
    plaintext = [""] * col
    currCol = 0
    currRow = 0

    for c in ciphertext:
        plaintext[currCol] += c
        currCol += 1
 
        if (
            (currCol == col)
            or (currCol == col - 1)
            and (currRow >= row - unoccupied)
        ):
            currCol = 0
            currRow += 1
 
    generatedPlainText = "".join(plaintext)
#TRANSPOSITION END

## VIGENERE START
def encryptVigenere(plaintext):
    global generatedCipherText
    global generatedKey
    plaintext = plaintext.upper()
    possibleKeyLengths = range(1, 27)
    useKeyLength = random.choice(possibleKeyLengths)
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tempKey = ""
    for i in range(useKeyLength):
        tempKey += random.choice(alphabets)
    tempCipherText = ""
    j = 0
    for i in range(len(plaintext)):
        if alphabets.find(plaintext[i]) == -1:
            tempCipherText += plaintext[i]
            j += 1
            j = j%len(tempKey)
            continue
        #print(str(plaintext[i]),"=",str(alphabets.find(plaintext[i]))," + ",generatedKey[j],"="+str(alphabets.find(generatedKey[j]))," = ")
        tempIndex = alphabets.find(plaintext[i]) + alphabets.find(tempKey[j])
        tempIndex = tempIndex%26
        #print(str(tempIndex),"=",alphabets[tempIndex])
        tempCipherText += alphabets[tempIndex]
        j += 1
        j = j%len(tempKey)

    generatedCipherText = tempCipherText
    generatedKey = tempKey

def decryptVigenere(ciphertext, key):
    global generatedPlainText
    ciphertext = ciphertext.upper()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tempPlainText = ""
    j = 0
    for i in range(len(ciphertext)):
        if alphabets.find(ciphertext[i]) == -1:
            tempPlainText += ciphertext[i]
            j += 1
            j = j%len(key)
            continue
        tempIndex = alphabets.find(ciphertext[i]) - alphabets.find(key[j])
        tempIndex = tempIndex%26
        tempPlainText += alphabets[tempIndex]
        j += 1
        j = j%len(key)

    generatedPlainText = tempPlainText
## VIGENERE: END

## CAESAR START

def encryptCaesar(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]

        if (char == " "):
            result += " "
            continue
 
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    
    generatedCipherText = result
    generatedKey = 3
    return result

def decryptCaesar(cipher):
    ## print ("test")
    result = ""

    for i in range(len(cipher)):
        char = cipher[i]

        if (char == " "):
            result += " "
            continue
 
        if (char.isupper()):
            result += chr((ord(char) - 3 - 65) % 26 + 65)

        else:
            result += chr((ord(char) - 3 - 97) % 26 + 97)
 
    return result
    
def shiftEncryption(plaintext):
    global generatedCipherText
    global generatedKey
    keyList = [i for i in range(1, 26)]
    key = random.choice(keyList)
    ciphertext = ""
    plaintext = plaintext.lower()

    for a in plaintext:
        if a.isupper():
            if(a == " "):
                ciphertext += " "
            else:
                oldIndex = ord(a) - ord("A")
                index = (oldIndex + key) % 26
                newUnicode = index + ord("A")
                finalChar = chr(newUnicode)
                ciphertext = ciphertext + finalChar
        else:
            if(a == " "):
                ciphertext += " "
            else:
                oldIndex = ord(a) - ord("a")
                index = (oldIndex + key) % 26
                newUnicode = index + ord("a")
                finalChar = chr(newUnicode)
                ciphertext = ciphertext + finalChar
    
    generatedCipherText = ciphertext
    generatedKey = key


def shiftDecryption(ciphertext, key):
    global generatedPlainText
    plaintext = ""
    key = int(key)
    ciphertext = ciphertext.lower()

    for a in ciphertext:
        if a.isupper():
            oldIndex = ord(a) - ord("A")
            index = (oldIndex - key) % 26
            newUnicode = index + ord("A")
            finalChar = chr(newUnicode)
            plaintext = plaintext + finalChar
        else:
            oldIndex = ord(a) - ord("a")
            index = (oldIndex - key) % 26
            newUnicode = index + ord("a")
            finalChar = chr(newUnicode)
            plaintext = plaintext + finalChar
            
    generatedPlainText = plaintext

def monoencrypt(plaintext):
    global generatedCipherText
    global generatedKey
    plaintext = plaintext.lower()
    key = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz "

    for letter in plaintext:
        if letter in alphabet and letter not in key and letter != " ":
            key += letter

    for letter in key:
        if letter in alphabet and letter not in key and letter != " ":
            key += letter

    for letter in alphabet:
        if letter not in key:
            key += letter

    #key += " "

    indv = [alphabet.index(letter) for letter in plaintext]
    generatedCipherText = "".join(key[indk] for indk in indv)
    generatedKey = key

def monodecrypt(ciphertext, key):
    global generatedPlainText
    ciphertext = ciphertext.lower()
    key = key.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
            
    indv = [key.index(letter) for letter in ciphertext]
    generatedPlainText = ''.join(alphabet[indk] for indk in indv)

    ## cipher = input("Enter the text you wish to decrypt:\n")
    ## generatedPlainText = decryptCaesar(cipher)

    ## print ("Encoded Cipher: " + cipher)
    ## print ("Decrypted Message: " + decryptCaesar(cipher))

## CAESAR END

##PORTA START

alpha = {
    "A": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    "B": ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"),
    "C": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
    "D": ("ABCDEFGHIJKLM", "ZNOPQRSTUVWXY"),
    "E": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    "F": ("ABCDEFGHIJKLM", "YZNOPQRSTUVWX"),
    "G": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    "H": ("ABCDEFGHIJKLM", "XYZNOPQRSTUVW"),
    "I": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
    "J": ("ABCDEFGHIJKLM", "WXYZNOPQRSTUV"),
    "K": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    "L": ("ABCDEFGHIJKLM", "VWXYZNOPQRSTU"),
    "M": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
    "N": ("ABCDEFGHIJKLM", "UVWXYZNOPQRST"),
    "O": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    "P": ("ABCDEFGHIJKLM", "TUVWXYZNOPQRS"),
    "Q": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
    "R": ("ABCDEFGHIJKLM", "STUVWXYZNOPQR"),
    "S": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    "T": ("ABCDEFGHIJKLM", "RSTUVWXYZNOPQ"),
    "U": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
    "V": ("ABCDEFGHIJKLM", "QRSTUVWXYZNOP"),
    "W": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
    "X": ("ABCDEFGHIJKLM", "PQRSTUVWXYZNO"),
    "Y": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
    "Z": ("ABCDEFGHIJKLM", "OPQRSTUVWXYZN"),
}
 
 
def gtable(key):

    return [alpha[char] for char in key.upper()]
 
 
def encryptPorta(key, words):

    cipher = ""
    c = 0
    table = gtable(key)
    for char in words.upper():
        cipher += gopp(table[c], char)
        c = (c + 1) % len(table)
    return cipher
 
 
def decryptPorta(key, words):

    return encryptPorta(key, words)
 
 
def gpos(table, char):

    if char in table[0]:
        row = 0
    else:
        row = 1 if char in table[1] else -1
    return (None, None) if row == -1 else (row, table[row].index(char))
 
 
def gopp(table, char):

    row, col = gpos(table, char.upper())
    if row == 1:
        return table[0][col]
    else:
        return table[1][col] if row == 0 else char
 
    
## key = input("Enter Key: ")
## text = input("Enter text to Encrypt: ")
 
## print("Encrypted Message: " + encrypt(key, text))
## print("Decrypted Message: " + decrypt(key, encrypt(key, text)))

##PORTA END


## PLAYFAIR START

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


def decryptPlayfair(cipherText, keyword):
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
    # print(matrix_5x5)
    return cipher
## PLAYFAIR END



## STREAM START
def toBinary(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

def repeat_key(length):
    keyString = ""
    for i in range(length):
        if i < 3:
            keyString += "0"
        else:
            keyString += str(random.randint(0, 1))
    return keyString

def encrypt_stream(plaintext):
    global generatedCipherText
    global generatedKey
    result = []
    key = []
    binary = []
    for i in plaintext:
        binary.append(toBinary(i))
    for x in range(len(binary)):
        temp = '.'.join(str(t) for t in binary[x])
        string = repeat_key(len(temp))
        key.append(string)
        y = int(str(temp), 2) ^ int(string, 2)
        result.append(y)
    binary.clear()
    for z in result:
        binary.append(chr(z))
    generatedCipherText = ''.join(binary)
    generatedKey = ','.join(key)

def decryptStream(cipher, key):
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
## STREAM END
def main():
    print("Welcome to _________")
    userResponse = input("Enter 'encrypt' to encrypt a text or 'decrypt' to decrypt a text. Enter 'q' to exit the program: ")
    print("")
    while(userResponse != "q"):
        if userResponse == "encrypt":
            output = []
            #flag will be true if it is the second time encrypting
            flag = 0
            value = 1
            option = ""
            userCipher = ""
            while(value):

                print("Which of the following ciphers was used to encrypt the text: ")
                print("1. Vigenere Cipher")
                print("2. Transposition Cipher")
                print("3. Caesar Cipher")
                print("4. Shift Cipher")
                print("5. Monoalphabetic Substitution Cipher")
                print("6. Porta Cipher")
                print("7. Playfair Cipher")
                print("8. Stream Cipher")
                print("9. Hill Cipher")
                userCipher = ""

                while(not isinstance(userCipher, int)):
                    userCipher = input("Please enter the corresponding number: ")
                    try:
                        userCipher = int(userCipher)
                    except ValueError:
                        print("Please enter an integer!")

                while((userCipher < 1 or userCipher > 9) and flag == 0):
                    userCipher = input("Please enter the corresponding number: ")
                    userCipher = int(userCipher)
                if flag == 0:
                    if option != 'y' and option != 'Y':
                        userPlainText = input("Please enter the plaintext that you want to encrypt: ")
                    else:
                        print("Your encrypted text for previous level is",generatedCipherText)
                        print("Your key for previous level is",generatedKey)
                        print("Keep note of all encrypted texts and keys as you will have to enter them in reverse order to decrypt")
                        userPlainText = generatedCipherText
                if userCipher == 1:
                   #vigenereencrypt
                   #if flag == false use userPlaintext
                   #else use output[-1]
                   encryptVigenere(userPlainText)
                   output.append("vigenere")
                   output.append(generatedKey)
                   output.append(generatedCipherText)
                
                elif userCipher == 2:
                   #transpositionencrypt
                   encryptTransposition(userPlainText)
                   output.append("transposition")
                   output.append(generatedKey)
                   output.append(generatedCipherText)
                  
                elif userCipher == 3:
                   #caesarencrypt
                   #encryptCaesar(userPlainText, 3)
                   output.append("caesar")
                   output.append(3)
                   output.append(encryptCaesar(userPlainText, 3))
                   generatedCipherText = encryptCaesar(userPlainText, 3)
                   generatedKey = 3
                   
                elif userCipher == 4:
                   #shiftencrypt
                   shiftEncryption(userPlainText)
                   output.append("shift")
                   output.append(generatedKey)
                   output.append(generatedCipherText)
                  
                elif userCipher == 5:
                   #monoencrypt
                   monoencrypt(userPlainText)
                   output.append("monoalphabetic")
                   output.append(generatedKey)
                   output.append(generatedCipherText)
                   
                elif userCipher == 6:
                   #portaencrypt
                   portaKey = input("Enter Key: ")
                   encryptPorta(portaKey, userPlainText)
                   output.append("porta")
                   output.append(portaKey)
                   output.append(encryptPorta(portaKey, userPlainText))
                   generatedCipherText = encryptPorta(portaKey, userPlainText)
                   generatedKey = portaKey
                  
                elif userCipher == 7:
                   #playfairencrypt
                   playFairKey = input("Enter Key: ")
                   encryptPlayfair(userPlainText, playFairKey)
                   output.append("playfair")
                   output.append(playFairKey)
                   output.append(encryptPlayfair(userPlainText, playFairKey))
                   generatedCipherText = encryptPlayfair(userPlainText, playFairKey)
                   generatedKey = playFairKey
                elif userCipher == 8:
                   #streamencrypt
                   encrypt_stream(userPlainText)
                   output.append("stream")
                   output.append(generatedKey)
                   output.append(generatedCipherText)
                   
                elif userCipher == 9:
                   #hillencrypt
                   output.append("hill")
                   output.append(generatedKey)
                   output.append(generatedCipherText)

                else:
                    print("Invalid Input")
                
                #choice to encrypt again
                option = input("Would you like to encrypt again? Y/N: ")
                #if yes is chosen, we go back to the top, nothing is input but what cipher to use, for plaintext we use previous ciphertext
                if option == 'y' or option == 'Y':
                    flag == 1
                    value = 1
                    continue
                #option for no
                if option == 'n' or option == 'N':
                    #layout for how info will be displayed
                    print("Cipher Type, Key, Ciphertext")
                    for x in output:
                        #will add a newline once a cipher type, key, and ciphertext is printed
                        #if len(output) % 3 == 0:
                        #    print("\n")
                        #else:
                            #prob wrong 
                        #    print(x + ", ")
                        print(x,"\n")
                    #ends code
                    break
        elif userResponse == "decrypt":
            print("Which of the following ciphers was used to encrypt the text: ")
            print("1. Vigenere Cipher")
            print("2. Transposition Cipher")
            print("3. Caesar Cipher")
            print("4. Shift Cipher")
            print("5. Monoalphabetic Substitution Cipher")
            print("6. Porta Cipher")
            print("7. Substitution Cipher")
            print("8. Stream Cipher")
            print("9. Hill Cipher")
            userCipher = ""
            while(not isinstance(userCipher, int)):
                userCipher = input("Please enter the corresponding number: ")
                try:
                    userCipher = int(userCipher)
                except ValueError:
                    print("Please enter an integer!")
            while(userCipher < 1 or userCipher > 9):
                userCipher = input("Please enter the corresponding number: ")
                userCipher = int(userCipher)
            userCipherText = input("Please enter the ciphertext that you want to decrypt: ")
            userKey = input("Please enter the key that was used to encrypt the ciphertext: ")
            if userCipher == 1:
                decryptVigenere(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
            elif userCipher == 2:
                try:
                    userKey = int(userKey)
                except ValueError:
                    print("Invalid key! An integer is required.")
                    print("Restarting...")
                    userResponse = input("Enter 'encrypt' to encrypt a text or 'decrypt' to decrypt a text. Enter 'q' to exit the program: ")
                    print("")
                    continue
                decryptTransposition(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
            elif userCipher == 3:
                generatedPlainText = decryptCaesar(userCipherText)
                print("The plaintext generated is ",decryptCaesar(userCipherText))
            elif userCipher == 4:
                shiftDecryption(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
            elif userCipher == 5:
                monodecrypt(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
            elif userCipher == 6:
                generatedPlainText = decryptPorta(userKey, userCipherText)
                print("The plaintext generated is ",decryptPorta(userKey, userCipherText))
            elif userCipher == 7:
                decryptPlayfair(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
            elif userCipher == 8:
                decryptStream(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
            elif userCipher == 9:
                decryptHill(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
        else:
            print("Invalid Input")
        userResponse = input("Enter 'encrypt' to encrypt a text or 'decrypt' to decrypt a text. Enter 'q' to exit the program: ")
        print("")

if __name__=="__main__":
    main()
