# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.

glass1 = "milk"
glass2 = "juice"

glass3 = glass1
glass1 = glass2
glass2 = glass3

print(glass1)
print(glass2)


#to check length of a string

a = "Yash here"
l =len(a)
print(l)

# to check the type of a variable

print(type("Yash"))
print(type(6969))
print(type(4.55))
print(type(True))

# type conversion or Type casting

print(int("48") + int("52"))

# practice question 

#solve the error in this = print("Number of letters in your name : " + (len(input("Enter your name : "))))
print("Number of letters in your name : " + str(len(input("Enter your name : "))))


# PEMDAS

#()
#exponents **
#*
#/
#+
#-

print(3*3+3/3-3)

# now to change this code so that answer will be or output will be 3 

print(3*(3+3)//3-3)

# number manipulation (use of f string)

iq = 69
cgpa = 8.1
got_placed = True
print(f"your iq is : {iq} , your cgpa is : {cgpa} and your placement status is : {got_placed}")
