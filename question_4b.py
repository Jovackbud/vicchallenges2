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
            print('Too low, try again')
        elif player_guess > expected_input:
            print('Too high, try again')
        player_guess = int(input('Guess a number between 1 to 1000:'))
    else:
        pass


def score_check():
    if counter < 10:
        print('Either you know the secret or you got lucky!')
    elif counter > 10:
        print('You should be able to do better!')
    else:
        print('Aha! You know the secret!')


guess_game()
score_check()
