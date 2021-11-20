def main():
    print("Welcome to _________")
    userResponse = input("Enter 'encrypt' to encrypt a text or 'decrypt' to decrypt a text. Enter 'q' to exit the program: ")
    print("")
    while(userResponse != "q"):
        if userResponse == "encrypt":
            output = []
            #flag will be true if it is the second time encrypting
            flag = false
            value = true
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

                while((userCipher < 1 or userCipher > 9) and flag == false):
                    userCipher = input("Please enter the corresponding number: ")
                    userCipher = int(userCipher)
                if flag == false:
                    userPlainText = input("Please enter the plaintext that you want to encrypt: ")
                if userCipher == 1:
                   #vigenereencrypt
                   #if flag == false use userPlaintext
                   #else use output[-1]
                   output.append("vigenere")
                   output.append(key)
                   output.append(ciphertext)
                
                elif userCipher == 2:
                   #transpositionencrypt
                   output.append("transposition")
                   output.append(key)
                   output.append(ciphertext)
                  
                elif userCipher == 3:
                   #caesarencrypt
                   output.append("caesar")
                   output.append(key)
                   output.append(ciphertext)
                   
                elif userCipher == 4:
                   #shiftencrypt
                   output.append("shift")
                   output.append(key)
                   output.append(ciphertext)
                  
                elif userCipher == 5:
                   #monoencrypt
                   output.append("monoalphabetic")
                   output.append(key)
                   output.append(ciphertext)
                   
                elif userCipher == 6:
                   #portaencrypt
                   output.append("porta")
                   output.append(key)
                   output.append(ciphertext)
                  
                elif userCipher == 7:
                   #subencrypt
                   output.append("substitution")
                   output.append(key)
                   output.append(ciphertext)
                   
                elif userCipher == 8:
                   #streamencrypt
                   output.append("stream")
                   output.append(key)
                   output.append(ciphertext)
                   
                elif userCipher == 9:
                   #hillencrypt
                   output.append("hill")
                   output.append(key)
                   output.append(ciphertext)

                else:
                    print("Invalid Input")
                
                #choice to encrypt again
                option = input("Would you like to encrypt again? Y/N")
                #if yes is chosen, we go back to the top, nothing is input but what cipher to use, for plaintext we use previous ciphertext
                if option == y or option == Y:
                    flag == true
                    continue
                #option for no
                if option == n or option == N:
                    #layout for how info will be displayed
                    print("Cipher Type, Key, Ciphertext")
                    for x in output:
                        #will add a newline once a cipher type, key, and ciphertext is printed
                        if len(output) % 3 == 0:
                            print("\n")
                        else:
                            #prob wrong 
                            print(x + ", ")
                    #ends code
                    break

                
