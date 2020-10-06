# calculating_distance
from math import sqrt


def calculating_distance(x1, y1, x2, y2):
    x_change = (x2 - x1) ** 2
    y_change = (y2 - y1) ** 2
    result = sqrt(x_change + y_change)
    print(result)


calculating_distance(int(input('Enter the first X coordinate: ')),
                     int(input('Enter the first Y coordinate: ')),
                     int(input('Enter the second X coordinate: ')),
                     int(input('Enter the second Y coordinate: ')))
