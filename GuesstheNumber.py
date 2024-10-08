#GuesstheNumber

import random

#Guess the computer's Number
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, Guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high. ')
    
    print(f'Congratuations, You have guess the number {random_number}')

# guess(10)

#Computer Guess our number
def computer_guess(x):
    print('The computer is trying to guess the number you are thinking of. Please only pick positive whole numbers less than or equal to 10.')
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low# could also be high b/c low = high
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high =  guess -1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(10)