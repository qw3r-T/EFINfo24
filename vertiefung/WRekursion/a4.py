def isprime(x):
    prim = False
    if x!=0 or x!=1:    
        prim = True
        for i in range(2,x//2):
            if x%i==0:
                prim = False
    
    return prim
    
def ispprime(x):
    if x in [2,3,5,7,23,37,53,73,373]:
        return True
    else:
        return False    

