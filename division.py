from random import randint

right_answers = 0
total_question = 0


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
        print(right_response[randint(1, 4)])
    else:
        wrong_response = {1: 'No, please try again!', 2: 'Wrong, try once more', 3: 'Don`t give up!',
                          4: 'No, keep trying!'}
        print(wrong_response[randint(1, 4)])
    total_question += 1


def comp_division():
    while total_question < 10:
        division_learning()
    else:
        scoring()


# checking to score
def scoring():
    score = (right_answers / total_question) * 100
    print(f'You scored {score} %')
    if score < 75:
        print('Please ask your teacher for extra help')
    else:
        print('Congratulations, you are ready to go to the next level' + '\n')


comp_division()
