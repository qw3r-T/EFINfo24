def ganzzahldivision(n,m,a=0):
    if n<m:
        return a
    else:
        return ganzzahldivision(n-m,m,a+1)

def modulo(n,m):
    if n<m:
        return n
    else:
        return modulo(n-m, m)

a=15
b=4
print(ganzzahldivision(a,b),'rest',modulo(a,b))

