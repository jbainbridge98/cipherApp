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
 
 
def encrypt(key, words):

    cipher = ""
    c = 0
    table = gtable(key)
    for char in words.upper():
        cipher += gopp(table[c], char)
        c = (c + 1) % len(table)
    return cipher
 
 
def decrypt(key, words):

    return encrypt(key, words)
 
 
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
 
    
key = input("ENTER KEY: ")
text = input("ENTER TEXT TO ENCRYPT: ")
 
print("ENCRYPTED: " + encrypt(key, text))
print("DECRYPTED WITH KEY: " + decrypt(key, encrypt(key, text)))
