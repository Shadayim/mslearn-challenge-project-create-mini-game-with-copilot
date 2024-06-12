#there 3 rules
# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.

# write a function that allows me to input either rock, paper, or scissors
# the function should randomly select rock, paper, or scissors for the computer
# the function should compare the user input to the computer's selection
# the function should print the result of the game
# the function should return the result of the game

#call the rock_paper_scissors function with the user input as an argument
#allow the user to enter their input in the 
#rock_paper_scissors function
#use the input function to allow the user to enter their input
#store the user input in a variable
#call the rock_paper_scissors function with the user input as an argument
#print the result of the game


import random

def rock_paper_scissors(user_input):
    computer_input = random.choice(['rock', 'paper', 'scissors'])
    if user_input == computer_input:
        return 'It\'s a tie!'
    elif user_input == 'rock':
        if computer_input == 'paper':
            return 'Computer wins!'
        else:
            return 'User wins!'
    elif user_input == 'paper':
        if computer_input == 'scissors':
            return 'Computer wins!'
        else:
            return 'User wins!'
    elif user_input == 'scissors':
        if computer_input == 'rock':
            return 'Computer wins!'
        else:
            return 'User wins!'
    else:
        return 'Invalid input!'
    

user_input = input('Enter rock, paper, or scissors: ')
result = rock_paper_scissors(user_input)
print(result)
