

from random import shuffle

mylist = ['empty','ball','empty']


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Pick a number:0, 1 or 2')

        return int(guess)

def check_answer(mylist,guess):
    if mylist[guess]=="ball":
        print('Correct.')
    else:
        print('Wrong.')
        print(mylist)


shuffled_list = shuffle_list(mylist)

guess=player_guess()

check_answer(shuffled_list,guess)