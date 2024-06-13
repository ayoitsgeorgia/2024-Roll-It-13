
# checks that users enter an integer
# that is more than 13
def int_check():
    while True:

        error = "please enter an integer that is 13 or more"

        try:
            response = int(input("Enter an integer: "))

            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                print("Your Number is ", response)
        except ValueError:
            print(error)


# main routine goes here
target_score = int_check()
print(target_score)
