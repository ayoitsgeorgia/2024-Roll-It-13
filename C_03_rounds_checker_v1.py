# checks for an integer more than 0 (allows <enter>)
def int_check(to_check):
    while True:

        error = "please enter an integer that is 1 or more"

        # check for infinite mode
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                # print(error)
                return "invalid"
            else:
                return response

        except ValueError:
            # print(error)
            return "invalid"


# Check that users have entered a valid
# option based on a list
def string_checker(user_response, valid_ans):
    while True:

        # Get user response and make sure it's lowercase
        user_response = user_response.lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        return "invalid"


# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ('xlif', 'invalid'),
    ('0.5', 'invalid'),
    ('0', 'invalid'),
    (1, 1),
    (2, 2),
    ('', "infinite"),
]

for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = int_check(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
