
print("Hey..Welcome to the PIZZA BUZZ")
size = input("What size pizza do u want S , M , L ,  : ")
pepporani = input("Do u want pepporani on your pizza ? Y or N : ")
extra_cheese = input("Do u want extra cheese ? Y or N ")
bill = 0
if size == "S":
   
        bill = 15
        
elif size == "M":
   
        bill = 20
elif size == "L":
   
        bill = 25
else :
        print("U entered a invalid text :( ")
if size == "S" and pepporani == "Y":
        
        bill += 2
elif size == "M" or "L" and pepporani == "Y":
        
        bill += 3
else :
        print("U entered a invalid text :( ")
if extra_cheese == "Y":
        bill +=1
else :
        print("U entered a invalid text :( ")

print(f"Your total bill is {bill} $")
    




