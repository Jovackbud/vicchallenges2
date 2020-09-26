from random import randint

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
    if answer == abs(a - b):
        right_response = {1: 'Very Good!', 2: 'Excellent', 3: 'Nice Work!', 4: 'Keep up the good work!'}
        print(right_response[randint(1, 4)])
        right_answers += 1
    else:
        wrong_response = {1: 'No, please try again!', 2: 'Wrong, try once more', 3: 'Don`t give up!',
                          4: 'No, keep trying!'}
        print(wrong_response[randint(1, 4)])
    total_question += 1


def scoring():
    score = (right_answers / total_question) * 100
    print(f'You scored {score} %')
    if score < 75:
        print('Please ask your teacher for extra help')
    else:
        print('Congratulations, you are ready to go to the next level' + '\n')


def comp_subtraction():
    while total_question < 10:
        subtraction_learning()
    else:
        scoring()
