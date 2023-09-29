from random import randint
from sys import stdout
from time import sleep

lower_num: int
higher_num: int
number_of_tries: int
number_of_attempts: int

introductory_text = "Hello!\ Let's randomly select an integer within the given range.\ Please provide the smallest and largest number to define the range."
introductory_text = introductory_text.split("\ ")

# print introduction
for _ in introductory_text:
    print(f"{str(_)}")
    sleep(1)

while True:
    # # add an animation
    # spinner = "-/|-\\|"
    # for _ in range(1, 10):
    #     for char in spinner:
    #         stdout.write(f'\r{char} ')
    #         stdout.flush()
    #         sleep(0.1)
    #
    # stdout.write('\r ')
    # stdout.flush()
    # print('')

    # enter the min and max to determine the range
    while True:
        try:
            lower_num = int(input("Enter lower number: "))
            higher_num = int(input("Enter higher number: "))
            if lower_num >= higher_num:
                raise ValueError("Lower number must be less than higher number")
            break
        except ValueError:
            print("Invalid input. Please enter valid integer values.")

    # add an animation again
    spinner = "-/|-\\|"
    for _ in range(1, 10):
        for char in spinner:
            stdout.write(f'\r{char} ')
            stdout.flush()
            sleep(0.1)
    stdout.write('\r ')
    stdout.flush()
    print('')

    print(f"Now, we will draw a whole number from {int(lower_num)} to {int(higher_num)}.", end="\n", flush=True)
    sleep(1)

    # add another animation
    for _ in range(10):
        print(".", end="", flush=True)
        sleep(0.2)
    sleep(1)
    first_random_number = randint(lower_num, higher_num)
    print(f"\nThe selected number is: {int(first_random_number)}", end='\n')
    sleep(1)

    number_of_draws = 0

    while True:
        second_random_number = randint(lower_num, higher_num)
        if second_random_number == first_random_number:
            break
        else:
            number_of_draws += 1
            continue
    sleep(1)

    # maximum number of attempts we allow the player
    number_of_tries = 5
    challenge_message = (
        f"Please guess how many times we need to draw a number from {int(lower_num)} to {int(higher_num)} to get {int(first_random_number)} again.\ You have {int(number_of_tries)} tries: ")
    challenge_message = challenge_message.split("\ ")

    # print challenge_message
    for _ in challenge_message:
        print(f"{str(_)}")
        sleep(1)
    sleep(1)

    # number of attempts used by the player
    number_of_attempts = 0
    # number of remaining attempts
    remaining_tries = number_of_tries - number_of_attempts

    while True:
        try:
            # the number guessed by the player
            user_guess: int = int(input())
        except ValueError as e:
            print("Please enter a valid number")

        number_of_attempts += 1
        remaining_tries -= 1

        if number_of_attempts <= 5:
            if user_guess > number_of_draws:
                print("The number is lower")
                print(f"{remaining_tries} tries left")
            elif user_guess < number_of_draws:
                print("The number is higher")
                print(f"{remaining_tries} tries left")
            else:
                print(f"You guessed the number in {number_of_attempts} tries!")
                break

        if number_of_attempts == 5:
            sleep(1)
            print(f"\nYou didn't guessed the number in {number_of_attempts} tries!")
            sleep(1)
            print(f"The correct number is {number_of_attempts}.")
            sleep(1)
            break

    print("")

    while True:
        try:
            user_input: int = int(input("If you want to play again, press 1. To exit, press 2: "))
            if user_input not in [1, 2]:
                raise ValueError("Please press 1 or 2: ")
            break
        except ValueError:
            print("Please press 1 or 2: ")

    if user_input == 1:
        continue
    if user_input == 2:
        sleep(1)
        print ("Thank you for playing!")
        break

