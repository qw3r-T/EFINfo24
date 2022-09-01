import math
def palindrome(word):
    for i in range(math.floor(len(word)/2)):
        if word[i-1] != word[-i]:
            return False
    return True

text = input('    > ')
print(palindrome(text))
