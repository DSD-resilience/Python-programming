import random

# Word list to start the game; there are mods with longer lists you can use
word_list = ["python", "hangman", "challenge", "program", "ascii"]

# Hangman ASCII art for each life left (from 6 down to 0)
stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========''',  # 0 lives
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''',  # 1 life
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''',  # 2 lives
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',  # 3 lives
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',  # 4 lives
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',  # 5 lives
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''',  # 6 lives (start)
]

# Pick a random word
word = random.choice(word_list)
word_display = ["_"] * len(word)
guessed_letters = []
lives = 6

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Game loop
while lives > 0 and "_" in word_display:
    print(stages[lives])
    print("Word:", " ".join(word_display))
    print("Guessed letters:", ", ".join(guessed_letters))

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!\n")
        for i in range(len(word)):
            if word[i] == guess:
                word_display[i] = guess
    else:
        print("Incorrect!\n")
        lives -= 1
