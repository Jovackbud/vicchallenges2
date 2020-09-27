# Create a function that receives an array of any amount of numbers and a single number. The function should return
# only the numbers that is a multiple of the number given in the array.


def multiples_only(num=2, *args):
    multiples = []
    for item in args:
        if item == num:
            pass
        elif item % num == 0:
            multiples.append(item)
    print(multiples)


multiples_only(int(input("Enter the divisor:")), tuple(input("Enter numbers to check:")))
