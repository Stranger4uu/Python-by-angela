# Runner-Up Score Program

# n = int(input("Enter number of scores: "))
# arr = list(map(int, input("Enter the scores: ").split()))

# Remove duplicates
# unique_scores = list(set(arr))

# Sort the list
# unique_scores.sort()

# Print the second highest score
# print("Runner-up score:", unique_scores[-2])

#  function defination
''' def sum(a,b): # parameters
    s = a+b
    print(s)
    return s;

sum(5,7) # function call ; arguments

'''
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