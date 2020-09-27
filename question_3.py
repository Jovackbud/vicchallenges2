# calculating_distance
from math import sqrt


def calculating_distance(x1, y1, x2, y2):
    x = (x2 - x1) ** 2
    y = (y2 - y1) ** 2
    result = sqrt(x + y)
    print(result)


calculating_distance(int(input('Enter the first X coordinate: ')),
                     int(input('Enter the first Y coordinate: ')),
                     int(input('Enter the second X cordinate: ')),
                     int(input('Enter the second Y coordinate: ')))
