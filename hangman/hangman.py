import random

TITLE = 'H A N G M A N'

words = ['python', 'java', 'kotlin', 'javascript']


choice = input()
while not choice == 'exit':
    if choice == 'play':
        number_of_guesses = 8
        WORD = random.choice(words)
        guessed_word = list('-' * len(WORD))
        print(TITLE)
        print('Type "play" to play the game, "exit" to quit: ', end='')

        letters = []
        while number_of_guesses > 0:
            print()
            print(''.join(guessed_word))
            if '-' not in guessed_word:
                print('You guessed the word\nYou survived!')
                break
            print('Input a letter: ', end='')
            letter = input()
            if len(letter) > 1 or letter == '':
                print("You should input a single letter")
                continue
            if (not letter.islower()) or (not letter.isalpha()):
                print("Please enter a lowercase English letter")
                continue

            if letter in WORD:
                if letter not in guessed_word:
                    letters.append(letter)
                    for index, el in enumerate(WORD):
                        if el == letter:
                            guessed_word[index] = letter
                else:
                    print("You've already guessed this letter")

            else:

                if letter not in letters:
                    number_of_guesses -= 1
                    letters.append(letter)
                    print("That letter doesn't appear in the word")
                else:
                    print("You've already guessed this letter")

        if '-' in guessed_word:
            print('You lost!')
            print()
            print('Type "play" to play the game, "exit" to quit: ', end='')

    else:
        print('Type "play" to play the game, "exit" to quit: ', end='')
    choice = input()
