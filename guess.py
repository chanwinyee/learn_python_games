# This is a Guess the Number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input() 

number = random.randint(1,20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

for guessesTaken in range(6):
    print('Take a guess.') # Four spaces in front of "print"
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.') # Eight space in front of "print"

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break 

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number: 
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')

# Bonus Exercise: How can I create an in-game leader board?
# Bonus Exercise 2: How can I create a leader board that is outside this game?