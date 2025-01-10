import random

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have multiple chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
""")

levels = { 
    "1" : {"Easy": 10}, 
    "2" : {"Medium": 5}, 
    "3" : {"Hard": 3}
}

chances = input("Enter your choice: ")

while chances not in list(levels.keys()):
    print("Please enter a valid input.")
    chances = input("Enter your choice: ")

difficulty = list(levels[chances].keys())[0]
tries = levels[chances][difficulty]
solution = random.randrange(1, 101, 1)

print(f"""
Great! You have selected the { difficulty } level.
Let's start the game!
""")

guess = 0

while solution != guess and tries > 0:
    guess = int(input("Enter your guess: "))
    tries = tries - 1
    if guess == solution:
        attempts = levels[chances][difficulty] - tries
        print(f"""Congratulations! You guessed the correct number in { attempts } attempts.
        """)
        exit
    elif tries == 0:
        print("""I'm sorry but you don't have any guesses left.
        """)
    elif guess < solution:
        print(f"""Incorrect! The number is greater than {guess}.
        """)
    else:
        print(f"Incorrect! The number is less than {guess}.")