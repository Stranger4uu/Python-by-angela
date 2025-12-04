# used to generate any 2 int random number 
import random

random_1 = random.randint(1,10)
print(random_1)


#to generate random number between 0-1
random_2 = random.random() # we can also multiply it by any number like , 2,5,19,4 etc
print(random_2)



# used to generate any 2 float random number 

random_3 = random.uniform(1,10)
print(random_3)

#program of random toss 


random_toss = random.randint(0, 1)   # 0 = head, 1 = tail
guess = input("Enter your guess (Head/Tail): ").lower()

result = "head" if random_toss == 0 else "tail"
print("Toss result:", result.capitalize())

if guess == result:
    print("You guessed it right!")
else:
    print("Sorry, you guessed it wrong :(")
