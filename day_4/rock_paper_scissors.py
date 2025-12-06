import random

game_elements = ["Rock","Paper","Scissor"]
user_choice = input("Enter your choice Rock , Paper or Scissor : ").lower()
computer_choice = random.choice(game_elements)
print(f"Computer Choice :{computer_choice}")

if user_choice == "rock" and computer_choice == "Rock" :
    print("It's a draw")
elif user_choice == "paper" and computer_choice == "Paper" :
    print("It's a draw")
elif user_choice == "scissor" and computer_choice == "Scissor" :
    print("It's a draw")
elif user_choice == "rock" and computer_choice == "Paper" :
    print("Sry...You lost and computer wins")
elif user_choice == "rock" and computer_choice == "Scissor" :
    print("Congo...You won ")
elif user_choice == "paper" and computer_choice == "Rock" :
    print("Congo...You won ")
elif user_choice == "paper" and computer_choice == "Scissor" :
    print("Sry...You lost and computer wins ")
elif user_choice == "scissor" and computer_choice == "Rock" :
    print("Sry...You lost and computer wins ")
elif user_choice == "scissor" and computer_choice == "Paper" :
    print("Congo...You won")

# Better logic and short code 

import random

game_elements = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter Rock, Paper or Scissor: ")
computer_choice = random.choice(game_elements)

print(f"Computer Choice: {computer_choice}")

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == "Rock" and computer_choice == "Scissor") or \
     (user_choice == "Paper" and computer_choice == "Rock") or \
     (user_choice == "Scissor" and computer_choice == "Paper"):
    print("Congo...You won!")
else:
    print("Sry...You lost and computer wins")

