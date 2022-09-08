import random

def rateZahl(n):
    random_number =random.randint(1,n)
    actual_guess = 0
    guess_count = 0
    while True:
        actual_guess = int(input('Enter a number between 1 and {} > '.format(n)))
        guess_count += 1
    
        if actual_guess == random_number:
            if guess_count == 1:
                print('Well done! You needed 1 guess')
            else:
                print('Well done! You nedded {} guesses'.format(guess_count))
            break
        else:
            if actual_guess < random_number:
                print('To small')
            elif actual_guess > random_number:
                print('To big')

rateZahl(10)
