# Write a python program that will help an elementary school student learn multiplication

# import radint module
from random import randint

right_answers = 0
total_question = 0


def multiplication_learning():
    global right_answers
    global total_question

    # generate the random numbers and print the question
    a = randint(0, 9)
    b = randint(0, 9)
    answer = int(input('How much is {} multiplied by {}:'.format(a, b)))
    total_question += 1
    if answer == a * b:
        right_response = {1: 'Very Good!', 2: 'Excellent', 3: 'Nice Work!', 4: 'Keep up the good work!'}
        print(right_response[randint(1, 4)])
        right_answers += 1
    else:
        wrong_response = {1: 'No, please try again!', 2: 'Wrong, try once more', 3: 'Don`t give up!',
                          4: 'No, keep trying!'}
        print(wrong_response[randint(1, 4)])

# checking to score
    def scoring():
        if total_question < 3:
            multiplication_learning()
        else:
            score = (right_answers / total_question) * 100
            print(f'You scored {score} %')
            if score < 75:
                print('Please ask your teacher for extra help')
            else:
                print('Congratulations, you are ready to go to the next level' + '\n')

    scoring()
    right_answers = 0
    total_question = 0


# addition_learning


def addition_learning():
    global right_answers
    global total_question

    # generate the random numbers and print the question
    a = randint(0, 9)
    b = randint(0, 9)
    answer = int(input('How much is {} plus {}:'.format(a, b)))
    total_question += 1
    if answer == a + b:
        right_response = {1: 'Very Good!', 2: 'Excellent', 3: 'Nice Work!', 4: 'Keep up the good work!'}
        print(right_response[randint(1, 4)])
        right_answers += 1
    else:
        wrong_response = {1: 'No, please try again!', 2: 'Wrong, try once more', 3: 'Don`t give up!',
                          4: 'No, keep trying!'}
        print(wrong_response[randint(1, 4)])

    # checking to score
    def scoring():
        if total_question < 3:
            addition_learning()
        else:
            score = (right_answers / total_question) * 100
            print(f'You scored {score} %')
            if score < 75:
                print('Please ask your teacher for extra help')
            else:
                print('Congratulations, you are ready to go to the next level' + '\n')

    scoring()
    right_answers = 0
    total_question = 0


# subtraction-learning

def subtraction_learning():
    global right_answers
    global total_question

    # generate the random numbers and print the question
    a = randint(0, 9)
    b = randint(0, 9)
    answer = int(input('What is the difference between {} and {}:'.format(a, b)))
    total_question += 1
    if answer == abs(a - b):
        right_response = {1: 'Very Good!', 2: 'Excellent', 3: 'Nice Work!', 4: 'Keep up the good work!'}
        print(right_response[randint(1, 4)])
        right_answers += 1
    else:
        wrong_response = {1: 'No, please try again!', 2: 'Wrong, try once more', 3: 'Don`t give up!',
                          4: 'No, keep trying!'}
        print(wrong_response[randint(1, 4)])

    # checking to score
    def scoring():
        if total_question < 3:
            subtraction_learning()
        else:
            score = (right_answers / total_question) * 100
            print(f'You scored {score} %')
            if score < 75:
                print('Please ask your teacher for extra help')
            else:
                print('Congratulations, you are ready to go to the next level' + '\n')

    scoring()
    right_answers = 0
    total_question = 0


# division_learning


# level selection
def level_selection(level):
    if level == 1:
        addition_learning()
    elif level == 2:
        subtraction_learning()
    elif level == 3:
        multiplication_learning()
    elif level == 4:
        pass
    elif level == 5:
        pass
    else:
        pass


level_selection(int(input('What level do you want:')))
