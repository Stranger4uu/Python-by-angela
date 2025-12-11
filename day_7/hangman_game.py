import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

random_words = ["green", "fruit", "apple", "games", "ocean", "music", "planet", "river", "window", "sunshine"]


lives = 6
print("You have 6 lives and each time u guess wrong your lives will - by 1 ")
choosen_word = random.choice(random_words)


placeholder = ""
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

display = placeholder  # Initialize display with the placeholder

Game_over = False
correct_letters = []

while not Game_over:  # Fix the condition to use != for the game loop
    guess = input("Guess a letter : ").lower()

    display = ""

    for letter in choosen_word:
        if letter == guess:
            display += letter 
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in choosen_word:
        lives -=1 
        print("You lost a live")
        print(f"Now you have : {lives} lives ")
    if lives < 6:
        print(HANGMANPICS[6 - lives])
        
    if lives == 0:
        print("Game over! You have 0 lives left.")
        Game_over = True
        break

    
 
    if "_" not in display:
        Game_over = True
        print("You won.....")

print(choosen_word)