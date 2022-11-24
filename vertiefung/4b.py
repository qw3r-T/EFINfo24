def mod(x,y):
    if x-y<0:
        return x
    else:
        return mod(x-y,y)
        
print(mod(10,3))
