# Create a function that receives an array of any amount of numbers and a single number. The function should return
# only the numbers that is a multiple of the number given in the array.


number = int(input("Enter the number which multiple you want:"))
nums_to_check = [21, 4, 9, 8, 13, 40, 32, 18, 27, 31, 11, 29, 33, 37, 41]
multiples = []
for num in nums_to_check:
    if num % number == 0:
        multiples.append(num)
print(multiples)