# Write a python program that will help an elementary school student learn multiplication
from random import randint


def multiplication_learning():
    a = randint(0, 9)
    b = randint(0, 9)
    print('what is {} multiplied by {}'.format(a, b))

    answer = int(input('Enter your answer:'))
    if answer == a * b:
        print('Very Good!')
    else:
        while answer != a * b:
            print('No, try again')
            print('what is {} multiplied by {}'.format(a, b))
            answer = int(input('Enter your answer:'))
        else:
            print('Very Good!')

    print("enter 'N' to go to next question or 'E' to end")
    response_continue_or_not = str(input('Enter response here:'))
    if response_continue_or_not.upper() == 'N':
        multiplication_learning()
    elif response_continue_or_not.upper() == 'O':
        pass


multiplication_learning()
