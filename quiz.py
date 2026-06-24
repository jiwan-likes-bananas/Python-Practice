while True:
    score = 0
# score system to keep track of how many questions the user gets right.
    question_0 = input("What planet is known as the red planet?") .lower() .strip()
    if question_0 == ("mars"):
        print("correct.")
        score += 1
    else:
        print("incorrect.")
    question_1_list = ["pacific ocean", "pacific"]
# If they answer with either "pacific ocean" or "pacific" it will be correct, otherwise it will be incorrect.
    question_1 = input("what is the largest ocean in the world?") .lower() .strip()
    if question_1 in question_1_list:
        print("correct.")
        score += 1
    else:
        print("incorrect.")
    question_2 = input("What is the capital of United Kingdom?") .lower() .strip()
    if question_2 == ("london"):
        print("correct.")
        score += 1
    else:
        print("incorrect.")
    question_3 = input("What is the largest mammal?") .lower() .strip()
    if question_3 == ("blue whale"):
        print("correct.")
        score += 1
    else:
        print("incorrect.")
    question_4 = input("What is the chemical symbol for silver?") .lower() .strip()
    if question_4 == ("ag"):
        print("correct.")
        score += 1
    else:
        print("incorrect.")
    question_5_list = ["poison dart frog" , "golden poison frog", "dart frog"]
    question_5 = input("What is the most poisonous amphibian?") .lower() .strip()
    if question_5 in question_5_list:
        print("correct.")
        score += 1
    else:
        print("incorrect.")
    if score == 6:
        print("You got a perfect score!")
        exit()
# if the user gets a perfect score, the quiz will end.
    elif score == 0:
        print("You didn't get any questions right, the quiz will start over.")
# if the user gets a score of 0, the quiz will start over.
    else:
        print(f"Your final score is: {score}/6")
        while True:
            play_again = input("Do you want to restart? (yes/no)") .lower() .strip()
            if play_again == "yes":
                break
            elif play_again == "no":
                print("Thank you for answering!")
                exit()
            else:
                print("Invalid input.")
# if the user gets a score between 1 and 5, the quiz will ask if they want to try again. If they say yes, the quiz will start over. If they say no, the quiz will end. If they enter anything other than yes or no, it will ask them to enter a valid input.