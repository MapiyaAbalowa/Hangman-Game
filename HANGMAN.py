# This is  a HANGMAN game.
# by MapiyaAbalowa, University of the Philippines Visayas

#Import 

import random

#HANGMAN Pictures:

HANGMAN = (
"""

  -----------
  |         |
  |       EMPTY
  |
  |
  |
  |
  |
  |
  |
  --------------
""",
"""

  -----------
  |         |
  |         0
  |
  |
  |
  |
  |
  |
  |
  --------------
""",
"""

  -----------
  |         |
  |         0
  |       --+-- 
  |
  |
  |
  |
  |
  |
  --------------
""",
"""

  -----------
  |         |
  |         0
  |      /--+--
  |
  |
  |
  |
  |
  |
  --------------
""",
"""
  -----------
  |         |
  |         0
  |      /--+--/
  |
  |
  |
  |
  |
  |
  --------------
""",

"""
  -----------
  |         |
  |         0
  |      /--+--/
  |         |
  |
  |
  |
  |
  --------------

""",
"""
  -----------
  |         |
  |         0
  |      /--+--/
  |         |
  |         |
  |
  |
  |
  |
  --------------

""",
"""

  -----------
  |         |
  |         0
  |      /--+--/
  |         |
  |         |
  |        | |
  |
  |
  |
  --------------

""",
"""
  -----------
  |         |
  |         0
  |      /--+--/
  |         |
  |         |
  |        | |
  |        | |
  |
  |
  --------------

""",
"""
  -----------
  |         |
  |         0
  |      /--+--/
  |         |
  |         |
  |        | |
  |        | |
  |__________________
  |   WASTED!!!
  --------------

""")

#Greeting the player!

name = input("Hi there! Mind giving your name? >> ")
print("Hello,",name +"! Good Luck playing HANGMAN!")

#Creating the constant variables

WORDS = ["PYTHON", "JAVA", "CPP", "HTML", "CSS", "JAVASCRIPT", "CSHARP", "VISUAL BASIC"]

HINTS = ("A snake.", "An island in Indonesia.", "Communist Party of the Philippines.", "For web development.", "Styling websites", "An island in Indonesia with scripts.", "Just like teeth.", "Basic sight.")

WRONGMAX = len(HANGMAN)

wrong = 0

word = random.choice(WORDS)

pos_word = WORDS.index(word)

hint = HINTS[pos_word]

used = []

length = len(word)

blank = "-" * length

a_word = []

num = 0

while num != length:

    a = word[num]

    a_word.append(a)

    num += 1

b_blank = []

num = 0

while num != length:

    b = blank[num]

    b_blank.append(b)

    num += 1

print("Let's start playing Hangman,",name +"!")

print("The word to guess is:")

print(blank)

ans = input("Would you like a hint? >> ")

if ans.lower() == "yes":

    print("Here's your hint:", hint)

else:
    print("Alright, as you wish!")


while wrong < WRONGMAX and b_blank != a_word:

    print(HANGMAN[wrong])

    print("So far the word you guessed is: ")

    print(b_blank)

    guess = input("Type your guess here: ")

    guess = guess.upper()

    if guess not in a_word and guess in used:

        print("Sorry your guess isn't in the word!")
        print("Your used this letter already!")

    elif guess not in a_word and guess not in used:

        print("Sorry the letter of your guessed isn't found in the word!")

        used.append(guess)

        wrong += 1

    elif guess in a_word and guess in used:

        print("Sorry, you guessed this letter already!")

    elif guess in a_word and guess not in used:

        print("You guessed a letter it!")

        for number in range(length):

            if guess == a_word[number]:

                b_blank[number] = guess

        used.append(guess)

if wrong == WRONGMAX and b_blank != a_word:

    print("You have been hanged!")

    print("The correct word was: ")

    print(word)

elif wrong < WRONGMAX and b_blank == a_word:
    
    print(b_blank)

    print(word)

    print("Congratulations! You guessed the word!")

            
exit()
