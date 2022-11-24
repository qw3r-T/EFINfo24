def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
        return True

def primes(n):
    return [x for x in range (2,n) if is_prime(x)]
    
print(primes(100))
