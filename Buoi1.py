# a^b mode n

def power(a, b, n):
    # Initialize result
    res = 1

    a = a % n
     
    if (a == 0):
        return 0
 
    while (b > 0):
 
        # If y is odd, multiply x with result
        if ((b & 1) == 1):
            res = (res * a) % n 
 
        # y must be even now
        b = b >> 1  # y = y/2
        a = (a * a) % n  # Change x to x^2
 
    return res % n
 
  # Driver Code

def modInverse(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1
 
# Function to return gcd of a and b
def gcd(a, b):
    if (a == 0):
        return b
 
    return gcd(b % a, a)