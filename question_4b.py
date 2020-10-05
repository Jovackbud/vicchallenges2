# number guessing game

from random import randint

counter = 0


def guess_game():
    expected_input = randint(1, 1000)
    global counter
    counter = 0
    player_guess = int(input('Guess a number between 1 to 1000:'))
    while player_guess != expected_input:
        counter += 1
        if player_guess < expected_input:
            print('No!!!' + 'Too low, try again\n')
        elif player_guess > expected_input:
            print('No!!!' + 'Too high, try again\n')
        player_guess = int(input('Guess a number between 1 to 1000:'))
    else:
        print('Right Guess!!!\n')


def score_check():
    if counter < 10:
        print('You guessed right in less than ten(10) tries, Either you know the secret or you got lucky!\n')
    elif counter > 10:
        print('You guessed right after more than ten(10) tries, You should be able to do better!\n')
    else:
        print('You guessed right in exactly ten(10) tries, Aha! You know the secret!\n')


def full_game():
    full_guess = 0
    while full_guess < 1:
        full_guess += 1
        guess_game()
        score_check()

    else:
        print('Do you want to play again?')
        decision = int(input('Enter 1 to play again or any other key to end: '))
        if decision == 1:
            full_game()


full_game()
