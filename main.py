import random
import math

lowest_num = int(input("Enter Lowest Number:-  "))
highest_num = int(input("Enter Highest Number:- "))

if highest_num <= lowest_num:
    print("Please make sure the highest number is greater than the lowest number!")
else:
    
    x = random.randint(lowest_num, highest_num)

    guess = None
    guess_count = 0

    while guess != x:
        guess = int(input(f"Please guess a number between {lowest_num} and {highest_num}\n"))
        if guess == x:
            guess_count = guess_count + 1
            print(f"Good job! You guessed the right number, it was {x}")
            print(f"You guessed it in {guess_count} tries!")
            input("Press a key twice to quit")
        else:
            if guess < x:
                print("You need to guess higher")
            else:
                print("You need to guess lower")
            guess_count = guess_count + 1
