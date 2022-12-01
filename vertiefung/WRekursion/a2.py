def addition(a,b):
    if (b<0):
        if b==0:
            return a
        else:
            return addition(a-1,b+1)
    else:
        if b==0:
            return a
        else:
            return addition(a+1,b-1)
        
print(addition(3,3))


def sub(a,b):
    if (b<0):
        if b==0:
            return a
        else:
            return sub(a+1,b+1)
    else:
        if b==0:
            return a
        else:
            return sub(a-1,b-1)
            
print(sub(15,5))
