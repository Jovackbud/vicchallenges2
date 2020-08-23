# Write a python program that will help an elementary school student learn multiplication
from random import randint


def multiplication_learning():
    a = randint(0, 9)
    b = randint(0, 9)
    print('what is {} multiplied by {}'.format(a, b))

    answer = int(input('Enter your answer:'))
    if answer == a * b:
        right_response = {1: 'Very Good!', 2: 'Excellent', 3: 'Nice Work!', 4: 'Keep up the good work!'}
        print(right_response[randint(1, 4)])
    else:
        while answer != a * b:
            wrong_response = {1: 'No, please try again!', 2: 'Wrong, try once more', 3: 'Don`t give up!',
                              4: 'No, keep trying!'}
            print(wrong_response[randint(1, 4)])
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
