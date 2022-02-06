# https://edabit.com/challenge/2X2uZysLJ3CpsxLDD
from math import pi

def radians_to_degrees(n):
    angle = n * 180/pi
    print(round(angle, 1))

radians_to_degrees(1)
radians_to_degrees(5)
radians_to_degrees(7)
radians_to_degrees(60)
radians_to_degrees(100)
radians_to_degrees(180)

'''
radians_to_degrees(1), 57.3
radians_to_degrees(5), 286.5
radians_to_degrees(7), 401.1
radians_to_degrees(60), 3437.7
radians_to_degrees(100), 5729.6
radians_to_degrees(180), 10313.2
'''