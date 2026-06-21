def get_number():
    while True:
        num = input("Give me a number.")
        try:
            num = int(num)
            return
        except:
            print("That's not a number")

num = get_number()

print(num)