# 22 - Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.


heads = int(input("Enter no.of heads : "))
legs = int(input("Enter no.of legs : "))

dogs = (legs - (2 * heads)) // 2
chickens = heads - dogs

print(f"Chickens = {chickens}")
print(f"Dogs = {dogs}")