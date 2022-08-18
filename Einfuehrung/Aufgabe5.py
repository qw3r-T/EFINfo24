my_input = []
while True:
    my_input.append(input(' >'))
    if my_input[-1] == 'exit':
        for element in my_input:
            if element != 'exit':
               print(element)
        break
