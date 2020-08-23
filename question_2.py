# Create a function that receives an array of any amount of numbers and a single number. The function should return
# only the numbers that is a multiple of the number given in the array.


def multiples_only(*args, num=3):
    multiples = []
    for item in args:
        if item == 3:
            pass
        elif item % num == 0:
            multiples.append(item)
    print(multiples)


arrayA = [21, 4, 9, 8, 13, 40, 32, 18, 27, 31, 11, 29, 33, 37, 41]


multiples_only(21, 4, 9, 8, 13, 40, 32, 18, 27, 31, 11, 29, 33, 37, 41)
