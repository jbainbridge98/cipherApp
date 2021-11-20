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


def main():

    print("Welcome to _________")
    userResponse = input("Enter 'encrypt' to encrypt a text or 'decrypt' to decrypt a text. Enter 'q' to exit the program: ")
    print("")
    while(userResponse != "q"):
        if userResponse == "encrypt":
            print("Encryption")
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
                decryptTransposition(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
            elif userCipher == 3:
                decryptCaesar(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
            elif userCipher == 4:
                decryptShift(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
            elif userCipher == 5:
                decryptMonoalphabetic(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
            elif userCipher == 6:
                decryptPorta(userCipherText, userKey)
                print("The plaintext generated is ",generatedPlainText)
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
        userResponse = input("Enter \"encrypt\" to encrypt a text or \"decrypt\" to decrypt a text. Enter \"q\" to exit the program: ")
    

if __name__=="__main__":
    main()