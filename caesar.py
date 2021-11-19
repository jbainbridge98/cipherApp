def encrypt(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
 
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
    

text = input("Enter the text you wish to encrypt:\n")
s = 3

print ("Original Text : " + text)
print ("Cipher: " + encrypt(text,s))

def decrypt(cipher):
    result = ""

    for i in range(len(cipher)):
        char = cipher[i]
 
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
 
    return result
    

cipher = input("Enter the text you wish to decrypt:\n")
s = 3

print ("Encoded Cipher: " + cipher)
print ("Decrypted Message: " + decrypt(cipher))

