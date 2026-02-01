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

# average of 3 numbers

def avg_of_3_no(a,b,c):
    avg = (a+b+c)/3
    print(avg)
    

avg_of_3_no(4,4,8)

cities = ["awlar","jaipur","delhi",]
def len_of_cities(list):
    print(len(list))
    
    
len_of_cities(cities)

def elements_of_list(list):
    for item in list:
        print(item,end=" ")

elements_of_list(cities)
print()

# function to print factorial of n number
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)
        
factorial(5)

# function to check if the number is odd or even 

def even_or_odd(n):
    if n%2 == 0:
        print("EVEN")
    else:
        print("ODD")

even_or_odd(4)

# recursive function

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

def fact(n):
    if n == 0 or n == 1:
        return 1
    return fact(n-1) * n

print(fact(4))

''' call stack 
The call stack is how a program keeps track of which function is running right now.

Think of it like:

📚 A stack of books — you can only put a new book on top, and you can only remove the top one.

Call stack is a memory structure that stores function calls in a Last-In-First-Out (LIFO) order to manage program execution.

'''

