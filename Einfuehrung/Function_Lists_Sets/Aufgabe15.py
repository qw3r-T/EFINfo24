def umlaut(word):
    chars = ["ä","ö","ü","Ä","Ö","Ü"]
    for char in chars:
        if char in word:
            return True

def ohne_umlaute(text):
    text_list = text.split(' ')
    for word in text_list:
        if umlaut(word):
            text_list.remove(word)
    return " ".join(text_list)

print(ohne_umlaute("mein töxt mit Ümlaut"))