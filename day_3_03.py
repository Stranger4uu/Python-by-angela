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
bill = 0
if height >= 120:
    print("Congo...  You can ride")
    if age < 12:
        bill = 5
        print("You need to pay 5$ ")
    elif age <= 18:
        print("You need to pay 7$ ")
        bill = 7
    else :
        print("You need to pay 12$ ")
        bill = 12
    want_photos =input("Do you want to take photos ? if yes type y and if no type n : ")
    if want_photos == "y":
        bill += 3
    print(f"Your total bill is {bill}")
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

