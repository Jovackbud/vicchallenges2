# calculating_distance
def calculating_distance(x1, y1, x2, y2):
    result = (abs(x2 - x1), abs (y2 - y1))
    print(result)


calculating_distance(int(input('Enter the first X cordinate: ')),
 int(input('Enter the first Y cordinate: ')),
  int(input('Enter the second X cordinate: ')),
   int(input('Enter the second Y cordinate: ')))
