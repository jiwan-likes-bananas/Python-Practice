score = 0
question_0 = input("What planet is known as the red planet?") .lower() .strip()
if question_0 == ("mars"):
    print("correct.")
    score += 1
else:
    print("incorrect.")
# If they answer with either "pacific ocean" or "pacific" it will be correct, otherwise it will be incorrect.
question_1_list = ["pacific ocean", "pacific"]
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
elif score == 0:
    print("You didn't get any questions right.")
else:
    print(f"Your final score is: {score}/6")