import math
from fractions import Fraction
height, angle = map(int, input().split())
sinValue = math.sin(math.radians(angle))
print(math.ceil(height/sinValue))
