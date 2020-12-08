import key_Generator
import encryption
import decryption


if __name__ == '__main__':
   
    #Make the Keys
    print("Generate Keys for ((Z/p)^x, *): \n")
    keys = key_Generator.key_generate(20, 5)
    print("------------------------------")

    #Store the private Key
    priv = keys[1]

    #Store the public Key
    pub = keys[0]

    #Encryption
    M = input("Insert Message: ")
    ciphertext = encryption.encryption(pub, M)
    print("Ciphertext:", ciphertext)
    print("---------------------------")

    #Decryption
    decrypt = decryption.decryption(ciphertext[0], ciphertext[1], priv)
    msg = ''.join(decrypt)
    print("Decrypted: ", msg)
    



    