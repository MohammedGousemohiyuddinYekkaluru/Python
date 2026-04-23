# Write a program to find the euclidean distance between two coordinates.

import math

x_1 = 6
x_2 = 7
y_1 = 9
y_2 = 5

euclidean_distance = math.sqrt(((x_2 - x_1)**2) + ((y_2 - y_1)**2))

print(euclidean_distance)

# Another way

point_1 = (6, 9)
point_2 = (7, 5)

distance = math.dist(point_1, point_2)
print(distance)