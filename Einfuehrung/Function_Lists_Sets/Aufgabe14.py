def starts_with_d(text):
    word_list = text.split()
    d_word_list = []
    for word in word_list:
        if word[0] == 'd' or word[0] == 'D':
            d_word_list.append(word)
    return sorted(d_word_list)
