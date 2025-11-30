# print("Hey..Welcome to the rollercoaster")
# age = int(input("What's your age : "))
# height = int(input("Enter your height in cm : "))
# if height >= 120:
#     print("Congo...  You can ride")
#     if age > 18:
#         print("You need to pay 12$ ")
#     else:
#         print("You need to pay 7$ ")
# else:
#     print("You cannot ride because your height is less than 120 cm sorry :( ")

#  Or 

print("Hey..Welcome to the rollercoaster")
age = int(input("What's your age : "))
height = int(input("Enter your height in cm : "))
if height >= 120:
    print("Congo...  You can ride")
    if age < 12:
        print("You need to pay 5$ ")
    elif age > 12 and age <= 18:
        print("You need to pay 7$ ")
    elif age > 18:
        print("You need to pay 12$ ")
else:
    print("You cannot ride because your height is less than 120 cm sorry :( ")



# Bmi question
# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)


# # Write your code below 👇
# if bmi < 18.5:
#     print("underweight")
# elif bmi >= 18.5 and bmi < 25:
#         print("normal weight")
# elif bmi > 25:
#         print("overweight")

