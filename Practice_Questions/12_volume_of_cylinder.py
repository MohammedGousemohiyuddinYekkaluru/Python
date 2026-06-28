# 12 - Write a program to find the volume of the cylinder. Also find the cost when, when the cost of 1litre milk is 60Rs.

radius = int(input("Enter the radius (in cm): "))
height = int(input("Enter the height (in cm): "))

volume = round((3.14 * (radius ** 2) * height) / 1000, 3)

cost = volume * 60

print("Volume is {} liters & the cost is {} Rs.".format(volume, cost))