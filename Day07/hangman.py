import random

word_list = ["python", "java", "kotlin", "javascript"]
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []

while not game_over:

    print(f"You have {lives}/6 lives left.")

    display = ""
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed {guess}.")
        continue
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True

            print(f"IT WAS {chosen_word}. You lose!")

    if "_" not in display:
        game_over = True
        print("You win!")