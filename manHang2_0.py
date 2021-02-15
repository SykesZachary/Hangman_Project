### Hangman 2.0 | Built from the ground up | 06.12.2019

### package imports
import random
from definition import Definition
from hangman_Difficulty import Difficulty


### the meat and potatoes.
def hangman():
    print('Ok! I\'m ready for you to guess! ')
    print('You have 10 attempts!')
    guessesMade = []
    correctGuess = 0
    turn = 10
    ### while loop to keep user guessing until all parts added
    while turn > 0:
        attempt = input('Guess a letter: ')
        attempt = attempt.upper()
        if attempt in guessesMade:
            print('You\'ve already guessed that')
            continue
        guessesMade.append(attempt)
        ### new if statement
        if attempt in wordGuess:
            print('Remaining attempts: ', turn)
            for letter in wordGuess:
                if letter == attempt:
                    correctGuess += 1
            for letter in wordGuess:
                if letter in guessesMade:
                    print(letter, end=' ',)
                elif letter != guessesMade:
                    print('_ ', end=' ',)

            if correctGuess == len(wordGuess):
                break

        elif attempt == 'word':
            for letter in wordGuess:
                if letter in guessesMade:
                    print(letter, end=' ',)
                elif letter != guessesMade:
                    print('_ ', end=' ',)

        elif attempt not in wordGuess and attempt != 'word':
            print('Sorry, not correct')
            turn -= 1
            print('Remaining attempts: ', turn)
            body_part(turn)
    ### end while loop
    if turn != 0:
        print('Congratulations! You won!')
        # Call a function with an api that calls a dictionary and returns the definition of the word
        Definition.definition_return()
    elif turn == 0:
        print('I\'m sorry, you lose')
        print('The answer was: ', wordGuess)
        # ask if they want the dictionary definition, call function
        Definition.definition_return()


### dictionary storing the body part gained per incorrect guess
def body_part(x):
    partBank = {9: 'a head', 8: 'a body', 7: 'an arm',
    6: 'another arm', 5: 'a leg', 4: 'another leg',
    3: 'a hand', 2: 'another hand', 1: 'a foot',
    0: 'another foot'}
    print('You earned', partBank[x])


### picks a random word from wordBank
def rand_selection(x):
    print('The word is ', str(len(wordGuess)), ' letters long')
    for letter in wordGuess:
        print('_ ', end=' ',)
    return hangman()


##### USER START #####
x = True
while x:
    print('Welcome to Hangman!')
    start = input('Shall we begin? [Y/n]: ')
    start = start.upper()
    if start == 'Y' and start.isalpha():
        x = False
        # fileCall()
        ### start difficulty parameters
        print('Please select a difficulty')
        diff_select = input('[Easy | Hard] ')
        diff_select = diff_select.upper()

        if diff_select == 'EASY' or diff_select == 'E':
            Diff = Difficulty()
            wordGuess = random.choice(Diff.easy_modify())
            rand_selection(wordGuess)
        elif diff_select == 'HARD' or diff_select == 'H':
            Diff = Difficulty()
            wordGuess = random.choice(Diff.hard_modify())
            rand_selection(wordGuess)
        else:
            print('Please make a valid selection')
            x = True

    elif start == 'N' and start.isalpha():
        print('Well that is unfortunate')
        break
    else:
        print('INVALID SELECTION')
        continue


##### NOTES #####
# use re.findall()
# don't append to wordBank until after difficulty.
# manipulate file before in a list (if possible)

# difficulty class should include three functions
# easy, medium, hard