# checking if three numbers can make a triangle


def triangle_check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print(True)
    else:
        print(False)


triangle_check(int(input('Enter the length of the first side:')),
               int(input('Enter the length of the first side:')),
               int(input('Enter the length of the first side:')))
