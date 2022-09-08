# a)
i = 0
j = 0
while i<5:
    while j<5:
        print(i,j)
        j += 1
    i += 1
    j = 0

print('\n\n\n\n')

# b)
i = 0
j = 0
while i<5:
    while j<=i:
        print(i,j)
        j += 1
    i += 1
    j = 0
