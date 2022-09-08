from random import randint
from time import sleep

def random_sleep():
    time = randint(1,5)
    sleep(time)
    print('I\'m done sleeping')
