import random


# Check that users have entered a valid
# option based on a list

def string_checker(question, valid_ans=("yes", "no")):
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


# Displays instructions
def instructions():
    print(''')

    **** Instructions ****

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


# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# compare user / computer choice and returns
# result (win/ tie/ lose)
def rps_compare(user, comp):
    # If the user and the computer choice is the same it's a tie
    if user == comp:
        round_result = "tie"

    # there are three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"

    # if it's not a win / tie then it's a loss
    else:
        round_result = "lose"

    return round_result


# Main Routine Starts here

# Initialise game variables
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("💎📃✂️ Rock / Paper / Scissors Game ✂️📃💎")
print()

# ask user if they want to see instructions and display them if requested

want_instructions = string_checker("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes" or want_instructions == "y":
    instructions()

print("The program will run")

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:
    # rounds headings
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode) "
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)
    print()

    # Randomly choose from the rps list (excluding exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print(" you chose", user_choice)

    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    # Adjust game lost / game tied counters and add results to game history
    if result == "tie":
        rounds_tied += 1
        feedback = "It's a tie"
    elif result == "lose":
        rounds_lost += 1
        feedback = "You lose"
    else:
        feedback = "You won"

    # Set up round feedback and output it user
    # add it to the game history list (include the round number)
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)
    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

if rounds_played > 0:
    # Game loop ends here

    # Game history / statistics

    # calculate stats
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # Output game statistics
    print(" Game Statistics")
    print(f" Won: {percent_won:.2f} \t "
          f" Lost: {percent_lost:.2f} \t "
          f" Tied: {percent_tied:.2f} \t")

    # ask user if they want to see their game  history and output if requested
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)
