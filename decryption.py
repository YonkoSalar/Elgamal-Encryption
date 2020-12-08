import main
import key_Generator
import struct
import math

#Finding multiplicative inverse 
def modInverse(a, m): 
    a = a % m 
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return 1


def decryption(c_1, c_2, priv):
    decrypt_msg = [] 

    #Same shared key that was used in encryption
    s = pow(c_1, priv.x, priv.p)
    print("Shared key: ", s )

    #Finding the multiplicative inverse of s modulo n
    s_inverse = modInverse(s, priv.p)
    print("Inverse S:", s_inverse)

    #Reverse values from 
    for i in range(0, len(c_2)):
        decrypt_msg.append(chr(int((c_2[i] *s_inverse)) % priv.p))
        
    return decrypt_msg


    

