word_list = []

while True:
    new_word = input('enter word > ')

    if new_word == 'letztes':
        word_list.append(new_word)
        break
    elif 'x' in new_word:
        continue
    elif new_word.count('e') >= 2:
        split_index = new_word.find('e')
        first_word = new_word[:split_index+1]
        second_word = new_word[split_index:]
        word_list.append(first_word)
        word_list.append(second_word)
    else:
        word_list.append(new_word)
print(word_list)
