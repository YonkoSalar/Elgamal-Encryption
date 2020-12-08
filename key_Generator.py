from random import randint
import random
import math
import sys


#Public Key Consist of G- Cyclic Group, q - order, g-generator, h - g^x 
class PublicKey(object):
    def __init__(self, p=None, g=None, h=None):
        self.p = p #Prime Number
        self.g = g #Generator
        self.h = h #h:=g^x(secret number)


class PrivateKey(object):
    def __init__(self, p=None, g=None, x=None ):
            self.p = p #Prime Number
            self.g = g #Generator
            self.x = x #Secret Value 


#Finding the gcd(a,b) were a is a > b
def gcd(a, b):
    while(b != 0):
        temp = a % b
        a=b
        b = temp
    return a
        

#Miller Rabin Test to check for primality test
def RabinTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = pow(a, d) % n
  
    if (x == 1 or x == n - 1): 
        return True 
  
    # Keep squaring x while one  
    # of the following doesn't  
    # happen 
    # (i) d does not reach n-1 
    # (ii) (x^2) % n is not 1 
    # (iii) (x^2) % n is not n-1 
    while (d != n - 1): 
        x = (x * x) % n
        d *= 2
  
        if (x == 1): 
            return False
        if (x == n - 1): 
            return True
  
    # Return composite 
    return False


#Checks if p is prime, and uses k as accurarcy parameter
def isPrime(p, k):
    # Typical cases where 
    if (p <= 1) or (p == 4):
        return False
    if (p <= 3): 
        return True 
  
    # Find r such that p = 2^d * r + 1 for some r >= 1 
    d = p - 1
    while (d % 2 == 0): 
        d //= 2
  
    # Iterate given nber of 'k' times 
    for i in range(k): 
        #Do the miller test to see if we have generated a prime
        if (RabinTest(d, p) == False): 
            return False
  
    return True 

#Generate prime number with number of bits and checks for primality
def generate_prime(NumBits=252, iConfidence=40):
    #Generate potential random prime
    while(1):
        p = random.randint( 2**(NumBits-2), 2**(NumBits-1))
        if(isPrime(p, iConfidence)):
            return p


def findGenerator(p):
    for i in range(2, p-1):
        if(gcd(i, p-1) == 1):
            return i



#We will generate a public key and private key
def key_generate(NumBits, iConfidence):
    #Generate a radnome prime number with NumBits being number of bits, and iConfidence number of checks
    prime = generate_prime(NumBits, iConfidence)

    print("Prime Number p:" , prime)

    #Fidning the smalles Primitve Root or generator of prime
    g = findGenerator(prime)
    
    print("Generator: ", g)

    #Random number between {1,..., p-1}
    x = random.randint( 1, (prime - 1) // 2 )
    print("Private Value: ", x)
    
    #Compute h = g^x
    h = pow(g, x, prime)

    #To compute the Public Key we must have (G, g, h, q)
    publicKey = PublicKey(prime, g, h)

    #To compute the Private Key we must have (G, g, x, q)
    privateKey = PrivateKey(prime, g, x)

    return publicKey, privateKey
