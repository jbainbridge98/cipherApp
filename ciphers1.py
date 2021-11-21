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
 
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

def decryptCaesar(cipher):
    ## print ("test")
    result = ""

    for i in range(len(cipher)):
        char = cipher[i]
 
        if (char.isupper()):
            result += chr((ord(char) - 3 - 65) % 26 + 65)

        else:
            result += chr((ord(char) - 3 - 97) % 26 + 97)
 
    return result
    

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
                   encryptCaesar(userPlainText, 3)
                   output.append("caesar")
                   output.append(generatedKey)
                   output.append(generatedCipherText)
                   
                elif userCipher == 4:
                   #shiftencrypt
                   output.append("shift")
                   output.append(generatedKey)
                   output.append(generatedCipherText)
                  
                elif userCipher == 5:
                   #monoencrypt
                   output.append("monoalphabetic")
                   output.append(generatedKey)
                   output.append(generatedCipherText)
                   
                elif userCipher == 6:
                   #portaencrypt
                   output.append("porta")
                   output.append(generatedKey)
                   output.append(generatedCipherText)
                  
                elif userCipher == 7:
                   #subencrypt
                   output.append("substitution")
                   output.append(generatedKey)
                   output.append(generatedCipherText)
                   
                elif userCipher == 8:
                   #streamencrypt
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
                option = input("Would you like to encrypt again? Y/N")
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
                decryptCaesar(userCipherText)
                print("The plaintext generated is ",decryptCaesar(userCipherText))
            elif userCipher == 4:
                decryptShift(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
            elif userCipher == 5:
                decryptMonoalphabetic(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
            elif userCipher == 6:
                decryptPorta(userKey, userCipherText)
                print("The plaintext generated is ",decryptPorta(userKey, userCipherText))
            elif userCipher == 7:
                decryptSubstituion(userCipherText, userKey)
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
