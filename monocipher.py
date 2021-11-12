#will change input when building UI
message = input("Enter message: ").lower()
#english alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
#will change input when building UI
inputKey = input("Enter key: ").lower()
#place holder for user input
key = ""
#users message input that will be manipulated
temp = ""
ciphertext = []

#checks to see if the users message input only contains items within the declared alphabet
for letter in message:
    if letter in alphabet:
        temp += letter

#checks if users key input only contains items within the declared alphabet and also makes sure there are no duplicate letters in key
for letter in inputKey:
    if letter in alphabet and letter not in key:
        key += letter

#if the key does not contain all 27 alloted characters this statement adds the rest of the alphabet
for letter in alphabet:
    if letter not in key:
        key += letter

#goes through temp and changes the message according to the key
def monoencrypt():
    indv = [alphabet.index(letter) for letter in temp]
    return "".join(key[indk] for indk in indv)

#takes key and changes letters accordingly
def monodecrypt():
    indv = [key.index(letter) for letter in cipher]
    return ''.join(alphabet[indk] for indk in indv)

cipher = monoencrypt()

print("Encrypted message :", cipher)
print("Decrypted message: ", monodecrypt())

