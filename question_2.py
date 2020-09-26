# Create a function that receives an array of any amount of numbers and a single number. The function should return
# only the numbers that is a multiple of the number given in the array.


def multiples_only(*args, num):
    multiples = []
    for item in args:
        if item == num:
            pass
        elif item % num == 0:
            multiples.append(item)
    print(multiples)


arrayA = [input('Enter the numbers you want to check seperated with commas: ')]
numA = int(input('Enter the number which multiple you want: '))


multiples_only(arrayA, numA)
