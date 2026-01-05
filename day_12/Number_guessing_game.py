import random
logo = """                                                                                                                                 
$$\   $$\                         $$\                                                                                   $$\                     
$$$\  $$ |                        $$ |                                                                                  \__|                    
$$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\         $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\ $$\ $$$$$$$\   $$$$$$\  
$$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$  __$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|$$ |$$  __$$\ $$  __$$\ 
$$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      $$ /  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\  $$ |$$ |  $$ |$$ /  $$ |
$$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |            $$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\ $$ |$$ |  $$ |$$ |  $$ |
$$ | \$$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |            \$$$$$$$ |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |
\__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|             \____$$ | \______/  \_______|\_______/ \_______/ \__|\__|  \__| \____$$ |
                                                                      $$\   $$ |                                                      $$\   $$ |
                                                                      \$$$$$$  |                                                      \$$$$$$  |
                                                                       \______/                                                        \______/                                                                   
"""
print(logo)

print("Welcome to the number guessing game :p ")
print("I am thinking of a number between 1 to 100 , and you need to guess that")
random_number = random.randint(1,100)
difficulty = input("Choose a difficulty 'Easy' or 'Hard' : ").lower()

if difficulty == "easy":
    attempt = 10
elif difficulty == "hard":
    attempt = 5

Game_over = False 
while Game_over == False:

    user_choice = int(input("Make a choice : "))

    if user_choice != random_number:
        attempt -= 1
        print(f"You have {attempt} attempts left")
        print(f"Guess again")

        if attempt == 0:
            print("You lost 😢, no attempts left.")
            print(f"The number was {random_number}")
            Game_over = True
            continue

        if random_number > user_choice:
            print("Guess a higher number ")
        else:
            print("Guess a lower number ")

    elif user_choice == random_number:
        print(f"Congo You guessed right , it was : {random_number} ")
        Game_over = True
