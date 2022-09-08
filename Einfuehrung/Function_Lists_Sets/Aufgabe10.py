def is_anagram(a,b):
    if sorted(list(a)) == sorted(list(b)):
        return True
    return False
