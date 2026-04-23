# Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

angle_1 = float(input("Enter angle 1 : "))
angle_2 = float(input("Enter angle 2 : "))
angle_3 = float(input("Enter angle 3 : "))

if angle_1 > 0 and angle_2 > 0 and angle_3 > 0 and (angle_1 + angle_2 + angle_3 == 180):
    print(f"{angle_1}, {angle_2}, {angle_3} forms a triangle")
else:
    print(f"{angle_1}, {angle_2}, {angle_3} cannot forms a triangle")


# Another way

def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0 and (a + b + c == 180):
        print("Yes, these angles form a valid triangle.")
    else:
        print("No, these angles do not form a triangle.")

print(is_triangle(angle_1, angle_2, angle_3))
