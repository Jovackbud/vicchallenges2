from random import randint

right_answers = 0
total_question = 0


def addition_learning():
    global right_answers
    global total_question

    # generate the random numbers and print the question
    a = randint(0, 50)
    b = randint(0, 50)
    answer = int(input('How much is {} plus {}:'.format(a, b)))
    if answer == a + b:
        right_response = {1: 'Very Good!', 2: 'Excellent', 3: 'Nice Work!', 4: 'Keep up the good work!'}
        print(right_response[randint(1, 4)] + '\n')
        right_answers += 1
    else:
        wrong_response = {1: 'No, please try again!', 2: 'Wrong, try once more', 3: 'Don`t give up!',
                          4: 'No, keep trying!'}
        print(wrong_response[randint(1, 4)] + '\n')
    total_question += 1


def subtraction_learning():
    global right_answers
    global total_question

    # generate the random numbers and print the question
    a = randint(0, 100)
    b = randint(0, 100)
    answer = int(input('What is the difference between {} and {}:'.format(a, b)))
    if answer == abs(a - b):
        right_response = {1: 'Very Good!', 2: 'Excellent', 3: 'Nice Work!', 4: 'Keep up the good work!'}
        print(right_response[randint(1, 4)] + '\n')
        right_answers += 1
    else:
        wrong_response = {1: 'No, please try again!', 2: 'Wrong, try once more', 3: 'Don`t give up!',
                          4: 'No, keep trying!'}
        print(wrong_response[randint(1, 4)] + '\n')
    total_question += 1


def multiplication_learning():
    global right_answers
    global total_question

    # generate the random numbers and print the question
    a = randint(0, 12)
    b = randint(0, 12)
    answer = int(input('How much is {} multiplied by {}:'.format(a, b)))
    if answer == a * b:
        right_response = {1: 'Very Good!', 2: 'Excellent', 3: 'Nice Work!', 4: 'Keep up the good work!'}
        print(right_response[randint(1, 4)] + '\n')
        right_answers += 1
    else:
        wrong_response = {1: 'No, please try again!', 2: 'Wrong, try once more', 3: 'Don`t give up!',
                          4: 'No, keep trying!'}
        print(wrong_response[randint(1, 4)] + '\n')
    total_question += 1


def division_learning():
    a = randint(1, 12)
    b = randint(1, 12)
    c = a * b
    print(f"What is {c} divided by {b}?")
    answer = int(input("Answer:"))

    global right_answers
    global total_question
    if answer == a:
        right_answers += 1
        right_response = {1: 'Very Good!', 2: 'Excellent', 3: 'Nice Work!', 4: 'Keep up the good work!'}
        print(right_response[randint(1, 4)] + '\n')
    else:
        wrong_response = {1: 'No, please try again!', 2: 'Wrong, try once more', 3: 'Don`t give up!',
                          4: 'No, keep trying!'}
        print(wrong_response[randint(1, 4)] + '\n')
    total_question += 1


def scoring():
    score = (right_answers / total_question) * 100
    print(f'You scored {score} %')
    if score < 75:
        print('Please ask your teacher for extra help')
    else:
        print('Congratulations, you are ready to go to the next level' + '\n')


def comp_addition():
    while total_question < 10:
        addition_learning()
    else:
        scoring()


def comp_subtraction():
    while total_question < 10:
        subtraction_learning()
    else:
        scoring()


def comp_multiplication():
    while total_question < 10:
        multiplication_learning()
    else:
        scoring()


def comp_division():
    while total_question < 10:
        division_learning()
    else:
        scoring()


def mixed_learning():
    while total_question < 10:
        pick = randint(1, 4)
        if pick == 1:
            addition_learning()
        elif pick == 2:
            subtraction_learning()
        elif pick == 3:
            multiplication_learning()
        else:
            division_learning()
    else:
        scoring()


# level selection
def level_selection(name, level):
    if level == 1:
        comp_addition()
    elif level == 2:
        comp_subtraction()
    elif level == 3:
        comp_multiplication()
    elif level == 4:
        comp_division()
    elif level == 5:
        mixed_learning()
    else:
        level_selection(str(input("Enter your name:")), int(input("Enter level here:")))
    print(f"Good bye {name.title()}. \n")


level_selection(str(input("Enter your name:")), int(input("Enter level here:")))
