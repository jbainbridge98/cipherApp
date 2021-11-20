import random
import math

class EncryptedText:
    
    def __init__(self, key, cipher, ciphertext):
        self.key = key
        self.cipher = cipher
        self.ciphertext = ciphertext

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

def encryptVigenere(plaintext):
    plaintext = plaintext.upper()
    possibleKeyLengths = range(1, 27)
    useKeyLength = random.choice(possibleKeyLengths)
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    generatedKey = ""
    for i in range(useKeyLength):
        generatedKey += random.choice(alphabets)
    generatedCipherText = ""
    j = 0
    for i in range(len(plaintext)):
        if alphabets.find(plaintext[i]) == -1:
            generatedCipherText += plaintext[i]
            j += 1
            j = j%len(generatedKey)
            continue
        #print(str(plaintext[i]),"=",str(alphabets.find(plaintext[i]))," + ",generatedKey[j],"="+str(alphabets.find(generatedKey[j]))," = ")
        tempIndex = alphabets.find(plaintext[i]) + alphabets.find(generatedKey[j])
        tempIndex = tempIndex%26
        #print(str(tempIndex),"=",alphabets[tempIndex])
        generatedCipherText += alphabets[tempIndex]
        j += 1
        j = j%len(generatedKey)
        
    encryptedObject = EncryptedText(generatedKey, "Vigenere", generatedCipherText)
    return encryptedObject

def decryptVigenere(ciphertext, key):
    ciphertext = ciphertext.upper()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    generatedPlainText = ""
    j = 0
    for i in range(len(ciphertext)):
        if alphabets.find(ciphertext[i]) == -1:
            generatedPlainText += ciphertext[i]
            j += 1
            j = j%len(key)
            continue
        tempIndex = alphabets.find(ciphertext[i]) - alphabets.find(key[j])
        tempIndex = tempIndex%26
        generatedPlainText += alphabets[tempIndex]
        j += 1
        j = j%len(key)
    
    return generatedPlainText


temp = encryptVigenere("Hello World")
print(temp.ciphertext)
smt = decryptVigenere(temp.ciphertext, temp.key)
print(smt)

temp = encryptTransposition("Hello World")
print(temp.ciphertext)
print(temp.key)
smt = decryptTransposition(temp.ciphertext, temp.key)
print(smt)



        
    