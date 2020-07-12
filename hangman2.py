import random 
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''','''
    +---+
    O   |
        |
        |
       ===''','''
    +---+
    O   |
    |   |
        |
       ===''','''
    +---+
    O   |
   /|   |
        |
       ===''','''
    +---+
    O   |
   /|\  |
        |
       ===''','''
    +---+
    O   |
   /|\  |
   /    |
    ===''','''
    +---+
    0   |
   /|\  |
   / \  |
       ===''']
words = {'Colours':'red orange yellow green blue indigo violet white black brown'.split(),
    'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
    'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
    'Animals':'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()}
    
def getRandomWord(wordDict):
    # This function returns a random string from the passed dictionary of lists of strings and its key.
    # First, randomly select a key from the dictionary:
    
    wordIndex = random.randint(0,len(wordList) -1) # Arrays start at 0
    return wordList[wordIndex] # the value in the brackets is the position number

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print ('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayboard(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + 'missed guesses and ' + str(len(correctLetters)) + 'correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True

        # Ask the player if they want to play again (but only if the game is done).
        if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord = getRandomWord(words)
                else:
                    break
# The spacing within the code matters