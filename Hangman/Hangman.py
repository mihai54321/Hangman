#my code

import random
from Hangman_words import word_list
import Hangman_art

print(Hangman_art.logo)
choosen_word = random.choice(word_list)
display = []
length = len(choosen_word)
life = 6
finisher = False


for letter in choosen_word:
    display += '_'

while finisher == False:
  	guess = input('Type your letter here. ').lower()

    if guess in display:
        print(f'You have already checked for {guess}.')

  	for i in range(length):
		char = choosen_word[i]
		# print(f"Current position: {i}\n Current letter: {char}\n Guessed letter: {guess}")
		if guess == char:
  			display[i] = char
  			print(display)

  	if guess not in choosen_word:
		life -= 1
		if life == 0:
  			finisher = True
  			print("Game Over! You lose!")
    print(f'{"".join(display)}')

  	if '_' not in display:
		finisher = True
		print('Game Over! You win!')

  	print(Hangman_art.stages[life])








# Angela Version

# import random

# #TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# #Delete this line: word_list = ["ardvark", "baboon", "camel"]
# from Hangman_words import word_list

# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# end_of_game = False
# lives = 6

# #TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# from Hangman_art import logo
# print(logo)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#     if guess in display:
#         print(f"You've already guessed {guess}")

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     #Check if user is wrong.
#     if guess not in chosen_word:
#         #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     #TODO-2: - Import the stages from hangman_art.py and make this error go away.
#     from Hangman_art import stages
#     print(stages[lives])