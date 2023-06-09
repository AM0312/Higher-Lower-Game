import data
import art
import random
import os

is_game_over = False
score = 0
acc1 = random.choice(data.data)
while not is_game_over:
    acc2 = random.choice(data.data)
    while acc1 == acc2:
        acc2 = random.choice(data.data)
    print(art.logo)
    print(f"Current Score: {score}")
    print(
        f"Compare A: {acc1['name']}, {acc1['description']}, from {acc1['country']}")
    print(art.vs)
    print(
        f"B: {acc2['name']}, {acc2['description']}, from {acc2['country']}")
    choice = input("Who has more Instagram Followers? A or B: ")
    if choice == "A" and acc1['follower_count'] >= acc2['follower_count']:
        score += 1
        acc1 = acc2
        os.system('cls')
    elif choice == "B" and acc2['follower_count'] >= acc1['follower_count']:
        score += 1
        acc1 = acc2
        os.system('cls')
    else:
        print("\n\nWrong Choice!")
        print("Game Over")
        is_game_over = True

print(f"Final Score: {score}")
