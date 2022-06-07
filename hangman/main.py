import random

#set lives
lives=6

#import
from word import word_list #import file from another location in 1 folder


#step1 : randome word from AI and display
from hangmanart import logo
print(logo)
print('!!--Welcome to hangman game--!!')
print("Guess The Letter")
choosen_word = random.choice(list(word_list))
print(choosen_word)



display=[]
word_lenght = len (choosen_word)
for char in range(word_lenght):
    display+="_"
print(f'Letter\t\t\t  : {display}')

end_of_game = False
while not end_of_game:
    guess = input("Guess The letter \t  : ").lower()

#step 4 : process to replace the blank
    if guess in display:
      print(f"u already type it{guess}")
    for position in range(word_lenght):
        letter = choosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in choosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -=1
        if lives==0:
          print("you lose")
          end_of_game = True
    if "_" not in display:
        end_of_game = True
        print("You Win")
    print(f"{' '.join(display)}")
    from hangmanart import stages
    print(stages[lives])