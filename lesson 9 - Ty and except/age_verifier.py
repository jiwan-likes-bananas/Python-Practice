# =====================================================================
# PROGRAM: Age verification
#           Verify the user's age is over 18 to give access (or deny access)
#           Keep asking for input until they've given a valid age
# =====================================================================

# VARIABLES
# TODO Create a variable for valid input and set it to false
valid_input = False
# GET INPUT
# TODO Start a loop while the input is invalid
while not valid_input:
    # TODO Ask the user for their age and save it
    age = input("What is your age?")
    #TRY
    # TODO Create a try statement
        # TODO Change the input into an integer and resave it
        # TODO Set the valid input variable to true
    try:
        age = int(age)
        valid_input = True
    # FAIL TO CONVERT TO INTEGER
    # TODO Add an except statement
    # TODO Tell the user their input was invalid
    except:
        print("Invalid input, try again.")
# Unindented = Loop has finished so the input must be valid now
valid_input = True
# CHECK AGE
# TODO Check if they are older than 18 and tell them they have access if they are
# TODO Check if they are older than 13 and tell them they have partial access if they are.
# TODO Otherwise tell them access has been denied
if age >= 18:
    print("You have full access!")
elif age >= 13:
    print("You have partial access!")
else:
    print("Access denied.")
# ===================================================================
# EXTENSION
# Create a avatar creator for them to use if they get access. There should be 2 versions (full and partial)
# Eg. Full can choose: character class (warrior, rogue), hair colour, eye colour; partial just character class (with animal classes?)