# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simpleguitk as simplegui
import random

secret_number = 0
range_high = 100
remaining_guesses = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, remaining_guesses
    print ""
    print "Guess a number between 0 and", range_high
    secret_number = random.randrange(0,range_high)
    if range_high == 100:
        remaining_guesses = 7
    else: 
        remaining_guesses = 10
    print "Number of guesses:", remaining_guesses


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_high
    range_high = 100
    print "Restarting Game!"
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_high
    range_high = 1000  
    print "Restarting Game!"
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global remaining_guesses
    remaining_guesses = remaining_guesses -1
    guess_number = int(guess)
    print "Guess was", guess_number
    if guess_number == secret_number:
        print "Correct"
        new_game()
    elif guess_number > secret_number:
        print "Lower"
        print "Remaining guesses:", remaining_guesses
    else:
        print "Higher" 
        print "Remaining guesses:", remaining_guesses
    if remaining_guesses < 1:
        print "You lost! Correct number was", secret_number
        new_game()
    
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_input("Enter a guess", input_guess, 200)
frame.add_button("Range 0 - 100", range100, 200)
frame.add_button("Range 0 - 1000", range1000, 200)

# register event handlers for control elements and start frame

frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
