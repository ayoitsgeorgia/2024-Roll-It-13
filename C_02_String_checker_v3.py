# Check that users have entered a valid
# option based on a list
def instructions():
    print(''')

    **** Paper, Scissors, Rock Instructions ****

To begin, decide the overall score needed to be crowned the winner of the game 
(eg: first person to get a score of 50 or more).

At the start of each round, the user and the computer each roll two dice. 
The initial number of points for each player is the total shown by the dice.
Then, taking turns, the user and computer each roll a single die and add the result to their points.  
The goal is to get 13 points (or slightly less) for a given round.
Once you are happy with your number of points, you can ‘pass’.

If you go over 13, then you lose the round (and get zero points). 
If the computer goes over 13, the round ends and your score is the number of points that you have earned.
If the computer gets more points than you (eg: you get 10 and they get 11, then you lose your score stays the same).  
If you get more points than the computer (but less than 14 points), you win and add your points to your score.
The computer’s score stays the same. 
If the first roll of your dice is a double, then your score is increased by double the number of points, provided you win. 
If the computer’s first roll of the dice is a double, then its points are not doubled (this gives the human player a slight advantage).

The ultimate winner of the game is the first one to get to the specified score goal.

Goodluck

    ''')


def string_checker(question, valid_ans=['yes', 'no']):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


# Main routine goes here

yes_no = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

# ask the user for their selection
user_choice = string_checker("What is your choice: ", rps_list)
print("You chose: ", user_choice)
