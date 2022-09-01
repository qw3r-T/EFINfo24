def primzahlen_finden(n):
    for number in range(1,n+1):
        if primzahl(number):
            print(number)
    
def primzahl(n):
    if n >= 2:
        for number in range(2,n):
            if n % number == 0:
                return False
        return True

n = int(input(' > '))
primzahlen_finden(n)
