import key_Generator
import main
import random
import math
import sys

def encryption(key, Message):
    c_2 = []
    m = Message

    #Chosses a random integer 
    y = random.randint(1, key.p - 1)
    print("y: ", y)
    
    #Shared Secret key
    s = pow(key.h, y, key.p)
    print("Shared key: ", s)

    #Maps every char into a list into the cyclic group
    for i in range(0, len(m)):
        #c_2.append(pow(key.g, ord(m[i]), key.p))
        c_2.append(ord(m[i])*s % key.p)
    
    #Compute the generator with exponent of a random integer y
    c_1 = pow(key.g, y, key.p) 
    
    return (c_1, c_2)
    
