def shiftEncryption(plaintext):
    keyList = [i for i in range(1, 26)]
    key = random.choice(keyList)
    ciphertext = ""

    for a in plaintext:
        if a.isupper():
            oldIndex = ord(a) - ord("A")
            index = (oldIndex + key) % 26
            newUnicode = index + ord("A")
            finalChar = chr(newUnicode)
            ciphertext = ciphertext + finalChar
        else:
            oldIndex = ord(a) - ord("a")
            index = (oldIndex + key) % 26
            newUnicode = index + ord("a")
            finalChar = chr(newUnicode)
            ciphertext = ciphertext + finalChar


def shiftDecryption(ciphertext, key):
    plaintext = ""

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
