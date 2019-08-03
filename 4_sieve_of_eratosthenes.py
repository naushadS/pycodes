import numpy as np

def soe(n):
    primes = [True for i in range(n+1)]
    primes[0] = False
    primes[1] = False
    for i in range(2, int(np.sqrt(n))+1):
        if primes[i]:
            k = 2
            while i*k <= n:
                primes[i*k] = False
                k += 1 
    return [index for (index, value) in enumerate(primes) if value]

if __name__ == '__main__':
    n = 36
    print(soe(n))




