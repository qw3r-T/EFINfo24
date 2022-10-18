def starts_with_d(text):
    word_list = text.split()
    d_word_list = []
    for word in word_list:
        if word[0] == 'd' or word[0] == 'D':
            d_word_list.append(word)
    return sorted(d_word_list)

def ends_with_e(text):
    word_list = text.split()
    word_list_e = []
    for word in word_list:
        if word[-1] == 'e':
            word_list_e.append(word)
    return sorted(word_list_e, key=len)
