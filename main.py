"""
The main file for my Integration Project
"""
__author__ = "Matt Toppi"

# imports----------
import time

# declaring values
end_program = 0


# functions----------------------------
def space():
    """
    A function that makes two lines of space. Used for neatness
    """
    print(" \n " * 2),


def time_two():
    """
    A function that makes the program sleep for 2 seconds before continuing
     to the next line of code
    """
    time.sleep(2),


# ---function showing off the use of strings---
def show_string():
    """
    A function that combines two strings that are inputted by the user
    """
    print("\nThis semester I learned about strings in python. \nHere is"
          " a simple application")
    time.sleep(1)
    phrase_one = input("Enter a word or phrase: ")
    phrase_two = input("Enter another word or phrase: ")
    space()

    print(phrase_one, phrase_two)
    space()
    print("Your two phrases have ben combined into one string"),


# ---function showing off use of operations---
def show_oper():
    """
    Function that has user input two numbers and manipulates them based
    off of simple algebra
    """
    oper = input(
        "What operation do you want to see. \nEnter one of the following"
        " corresponding numbers:\n1. +\n2. -\n3. *\n4. "
        "/\n5. //\n6. % \n\nWhich Operation: ")
    space()
    val_one = input("What is the first value you wish to calculate?: ")
    val_two = input("What is the second value you wish to calculate?: ")

    space()

    in_one = float(val_one)
    in_two = float(val_two)

    if oper == "1":
        print("The answer is", in_one + in_two)

    elif oper == "2":

        print("The answer is", in_one - in_two)

    elif oper == "3":
        print("The answer is", in_one * in_two)

    elif oper == "4":
        print("The answer is", in_one / in_two)

    elif oper == "5":
        print("The answer is", in_one // in_two)

    elif oper == "6":
        print("The answer is", in_one % in_two),


# this is the code for the number guessing game
def num_guess_game():
    """
    A guessing game that randomly selects a number and has the user guess said
     number
    """
    game_difficulty_value = 0
    import random

    print("\nNUMBER GUESSER")
    game_difficulty = input("\nWould you like the game to be EASY, MEDIUM, HAR"
                            "D, INSANE, or IMPOSSIBLE?: ")
    guess_cap = input("\nHow many guesses would you like to have?\nIF YOU WANT"
                      " THE DEFAULT OF TEN GUESSES, TYPE 'D'")

    if guess_cap == "D" or guess_cap == "d":
        guess_cap = 10

    if game_difficulty == "EASY" or game_difficulty == "easy":
        game_difficulty_value = 10

    elif game_difficulty == "MEDIUM" or game_difficulty == "medium":
        game_difficulty_value = 50

    elif game_difficulty == "HARD" or game_difficulty == "hard":
        game_difficulty_value = 100

    elif game_difficulty == "INSANE" or game_difficulty == "insane":
        game_difficulty_value = 500

    elif game_difficulty == "IMPOSSIBLE" or game_difficulty == "impossible":
        game_difficulty_value = 1000
    else:
        print("You did not input a correct option")

    print('\nTHE SYSTEM WILL RANDOMLY THINK OF A NUMBER BETWEEN 0 and',
          game_difficulty_value)
    print("\nYOU WILL HAVE", guess_cap, "GUESSES")

    random_num = random.randrange(0, game_difficulty_value, 1)
    # finding the random number

    guess_total = 0
    guess_remain = int(guess_cap)
    game_end = 0

    while guess_total <= int(guess_cap) and game_end == 0:
        print("WHAT IS YOUR GUESS AT THE NUMBER?: ")
        guess_num = int(input("-"))
        # guess_total = (guess_total + 1)
        guess_total += 1

        if guess_num < random_num:
            guess_remain = (guess_remain - 1)
            print("You are too LOW")
            print("Guesses remaining: ", guess_remain)

        if guess_num > random_num:
            guess_remain = (guess_remain - 1)
            print("You are too HIGH")
            print("Guesses remaining: ", guess_remain)

        if guess_num == random_num:
            guess_remain = (guess_remain - 1)
            print("YOU WIN")
            print("\nIt took you", guess_total, "guesses")
            game_end = 1

        if guess_remain == 1:
            print("THIS IS YOUR LAST GUESS")

        if guess_remain == 0:
            print("YOU LOSE")
            print("The random number is", random_num)
            game_end = 1,


def show_form():
    """
    A function that shows off formatting different numbers based off of their
     decimal values
    """
    print("\nThis function will showcase formatting")
    type_of_format = input("Enter the type of formatting you would like to "
                           "see.\n\n1. Aligning decimals\n2. Decimal "
                           "Length\n\n- ")

    if type_of_format == "1" or type_of_format == "Aligning decimals" or \
            type_of_format == "aligning decimals":
        print("\nYou will be asked to enter 3 numbers with decimals. The pro"
              "gram will print the numbers in an aligned "
              "format.")
        for_num1 = float(input("\nWhat is your first number?:"))
        for_num2 = float(input("What is your second number?:"))
        for_num3 = float(input("What is your third number?:"))
        print("\n")
        print("-" * 30)
        print("{:30.5f}".format(for_num1))
        print("{:30.5f}".format(for_num2))
        print("{:30.5f}".format(for_num3))
    elif type_of_format == "2" or type_of_format == "2" or type_of_format == \
            "Decimal length" or type_of_format == \
            "decimal length":
        for_num1 = float(input("Enter a number with decimals that will be fo"
                               "rmatted to the hundredths place: "))
        print("{:.2f}".format(for_num1))


def show_time():
    """
    A cool timer function that counts down from a certain numbers of time inp
    utted by the user
    """
    print("\nThis function is going to show the knowledge of the time functio"
          "n in python.")
    t_time = int(input("\nHow many seconds do you want the program to "
                       "wait?: "))
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    time_count = 0
    print("\n1...START...\n")
    while time_count < t_time - 2:
        time.sleep(1)
        time_count += 1
        print(time_count + 1, "...wait...")
    time.sleep(1)
    print()
    print(t_time, "...END...")
    time.sleep(3),


def show_mult_table():
    """
    Prints a multiplication table as large as the user wants
    """
    n = int(input('Positive integer between 1 and 10: '))
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            print(row * col, end="\t")
        print()


def selection_sort_func(nums):
    """
    Selection sort algorithm for sorting numbers
    """
    for x in range(len(nums)):
        lowest_value = x
        for j in range(x + 1, len(nums)):
            if nums[j] < nums[lowest_value]:
                lowest_value = j
        nums[x], nums[lowest_value] = nums[lowest_value], nums[x]


def bubble_sort_func(nums):
    """
    bubble sort algorithm for sorting numbers
    """
    swap = True
    while swap:
        swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swap = True


def show_sort():
    """
    A function that allows a user to input as many numbers as they wish then
     calls a user selected sorting algorithm
    """
    lst = []
    print("You will now enter numbers to put into a list that will be sorte"
          "d by the algorithm")
    list_tot = int(input("Enter number of elements : "))
    print("Enter", list_tot, "elements below:")
    for i in range(0, list_tot):
        ele = int(input())
        lst.append(ele)

    print("This is your list pre-sort\n", lst, "\n")
    print("These are the sorting algorithms I have codded.\n\n1. Selection\n2."
          " Bubble\n")
    type_sort = input("Which type of sort would you like to use?: ")
    if type_sort == "Selection" or type_sort == "selection" \
            or type_sort == "1":
        selection_sort_func(lst)

    if type_sort == "Bubble" or type_sort == "bubble" or type_sort == "2":
        bubble_sort_func(lst)
    print(lst)


print("\nThis program is going to showcase the things I have learned this"
      " semester during my COP1500 class.")
time.sleep(2)
while end_program == 0:
    # showing different functions
    print("-" * 100)
    print("Things learned: ")
    print("\n1. String - |Simple|\n(Use of: inputs, string combination)")
    print("\n2. Operations - |Simple|\n(Use of: float inputs, operations, if"
          "/elif)")
    print("\n3. Format - |Intermediate|\n(Use of: Formatting, if statements)")
    # print("\n4. Array\n")
    print("\n4. Time - |Intermediate|\n(Use of: loops, shortcut operators, s"
          "leep function)")
    print("\n5. Multiplication Table - |Intermediate|\n(Use of: Formatting, "
          "for loop statements")
    # projects
    print("-" * 100)
    print("Projects I worked on:")
    print("\n6. Sorts - |More Complex|\n(Use of: Algorithms, for loops, lis"
          "ts, appending lists, comparisons)")
    print("\n7. Guessing game - |More complex|\n(Uses: if/else, loops, boole"
          "ans, shortcut operators)")
    print("-" * 100)
    space()
    # noinspection SpellCheckingInspection
    chooseFunc = (input("Choose which topic you would like to see exhibited "
                        "(Type the name of topic or the correspondi"
                        "ng number): \n"))

    # execute the simple topics
    if chooseFunc == "1" or chooseFunc == "string" or chooseFunc == "String":
        show_string(),
    elif chooseFunc == "2" or chooseFunc == "Operations" \
            or chooseFunc == "operations":
        show_oper(),
    elif chooseFunc == "3" or chooseFunc == "Format" or chooseFunc == "format":
        show_form(),
    # elif chooseFunc == "4" or chooseFunc == "Array" or chooseFunc == "array":
    #   show_array(),
    elif chooseFunc == "4" or chooseFunc == "Time" or chooseFunc == "time":
        show_time(),
    elif chooseFunc == "5" or chooseFunc == "Multiplication table" \
            or chooseFunc == "multiplication table":
        show_mult_table()
    elif chooseFunc == "6" or chooseFunc == "Sorts" or chooseFunc == "sorts":
        show_sort()

    # execute the projects
    elif chooseFunc == "Guessing game" or chooseFunc == "guessing game" \
            or chooseFunc == "Guessing Game" or chooseFunc \
            == "7":
        num_guess_game(),
    else:
        print("You entered an incorrect option.")

    print("-" * 100)
    print("Would you like to go back to the main menu?")

    main_menu = input("Yes or no?: ")

    if main_menu == "no" or main_menu == "No" or main_menu == "NO":
        end_program = 1,

    print("\n" * 4)

print("Goodbye")
