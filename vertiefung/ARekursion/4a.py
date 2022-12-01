def pox(x,y):
    if y==1:
        return x;
    else:
        return x*pow(x,y-1)
        
print(pox(3,3))
