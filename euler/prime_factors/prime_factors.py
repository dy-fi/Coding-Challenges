import math

def largest_prime_factor(n): 
    maxi = -1

    # reduce n
    while(n % 2 == 0):
        maxi = 2
        n /= 2
    
    # search through possible primes, reducing n as we find factors
    for i in range(3, int(math.sqrt(n) + 1), 2):
        while n % i == 0:
            maxi = i
            n = n / i 

    return int(maxi)

if __name__ == '__main__':
    print(largest_prime_factor(600851475143))