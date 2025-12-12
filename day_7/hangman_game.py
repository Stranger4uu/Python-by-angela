import random
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


random_words = [
    "red", "blue", "green", "yellow", "pink", "purple", "orange", "black",
    "white", "gray", "cyan", "magenta", "maroon", "navy", "teal", "lime",
    "olive", "indigo", "violet", "turquoise", "beige", "brown", "gold",
    "silver", "coral", "peach", "lavender", "mint", "crimson", "skyblue"
]



lives = 6
print("You have 6 lives and each time u guess wrong your lives will - by 1 ")
chosen_word = random.choice(random_words)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

display = placeholder  # Initialize display with the placeholder

Game_over = False
correct_letters = []

while not Game_over:  # Fix the condition to use != for the game loop
    guess = input("Guess a letter : ").lower()
    if guess in display:
        print("You have already guessed this letter before , but don't worry you havent lost any lives this time ")


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter 
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("word to guess: " + display)
    

    if guess not in chosen_word:
        lives -=1 
        print(f"You lost a live because : {guess} is not in the word ")
        print(f"Now you have : ******** {lives} ******** lives ")
    if lives < 6:
        print(HANGMANPICS[6 - lives])
        
    if lives == 0:
        print("Game over! You have ******** 0 ******** lives left.")
        print(f"The word was : {chosen_word}")
        Game_over = True
        break

    
 
    if "_" not in display:
        Game_over = True
        print("******** You won..... ********")
        print(f"Correct the word is : {chosen_word}")
