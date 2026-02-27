import random

from hangman_words import word_list
from Art import stages,logo

word_list = ["aardvark", "baboon", "camel","abhishek","kundan","TANVI"]

print(logo)

chose_word = random.choice(word_list)
print(chose_word)

placeholder = ""

word_length = len(chose_word)

for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letter = []
lives = 6

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess A Letter: ").lower()

    if guess in correct_letter:
        print(f"You've already guessed a {guess}")

    display = ""

    for char in chose_word: 
        if char == guess:
            display += char
            correct_letter.append(guess)
        elif char in correct_letter:
            display += char
        else:
            display += "_"

    print(display)
    
    if guess not in chose_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chose_word}! YOU LOSE**********************")


    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    print(stages[lives])