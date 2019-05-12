import random

print('---------------------------------')
print('     Guess That Number Game')
print('---------------------------------')
print()

the_number = random.randint(0,100)
guess = -1

name  = input('What is your name?')

while guess != the_number:
    guess_text = input('Please guess a number from 1 to 100: ')
    guess= int(guess_text)
    if guess < the_number:
        print('Sorry {1}, your guess of {0} was too low'.format(guess,name))
    elif guess >the_number:
        print('Sorry {1},your guess of {0} too high'.format(guess,name))
    else:
        print('{}, you win!'.format(name))

print('done')


