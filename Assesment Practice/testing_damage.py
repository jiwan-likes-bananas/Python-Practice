Mob_hp = 100
dull_knife_damage = 3
user_input = input("You are in a dark room, you see a mob in front of you. What do you do? (attack/run) ").lower().strip()
if user_input == "attack":
    Mob_hp -= dull_knife_damage
    print(f"You attacked the mob with a dull knife, dealing {dull_knife_damage} damage. The mob's HP is now {Mob_hp}.")
elif user_input == "run":
    print("You ran away from the mob. Game over.")