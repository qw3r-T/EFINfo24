# a)
a_list = [i for i in range(1001) if i%7 == 0]
# b)
b_list = [i**3 for i in range(11)]
# c)
def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
        return True

c1_list = [[x,x+2,x+6] for x in range(995) if is_prime(x) and is_prime(x+2) and is_prime(x+6)]
c2_list = [[x,x+4,x+6] for x in range(995) if is_prime(x) and is_prime(x+4) and is_prime(x+6)]
c_list = c1_list + c2_list
print(c_list)
print(is_prime(6))
