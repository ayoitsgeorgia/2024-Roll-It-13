import random


# generates an integer between 0 and 6
# to simulate a roll of a die
def roll_die():
    result = random.randint(1, 6)
    return result


# Main Routine starts here
die_roll = roll_die()
print(die_roll)
