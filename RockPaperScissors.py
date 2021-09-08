def RPS():
    print("+----------------------------------------------+")
    print("| Winning Rules of the Rock-Paper-Scissors game |")
    print("|Rock vs. Paper --> Paper wins       |\n"
          "|Rock vs. Scissors --> Rock wins      |\n"
          "|Paper vs. Scissors --> Scissors wins  |")
    print("+----------------------------------------------+")
    yes_no = input("Do you want to play Rock-Paper-Scissors (Y/N)?")
    while True:
        Y_variable = "Y"
        y_variable = "y"
        if yes_no == y_variable or yes_no == Y_variable:
            print("Enter choice:\n" 
                           "1. Rock\n"
                           "2. Paper\n"
                           "3. Scissors ")
        else:
            print("Awww....\n"
              "Sorry to know that you do not want to play.\n"
              "Maybe next time.")
            quit()

        INVALID_INPUT = 0
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
        ask_choice = int(input("User turn:"))
        while ask_choice < INVALID_INPUT or ask_choice > SCISSORS:
                ask_choice = int(input("Enter a valid input:"))
        if ask_choice == ROCK:
            ask_pick = "Rock"
        elif ask_choice == PAPER:
            ask_pick = "Paper"
        elif ask_choice == SCISSORS:
            ask_pick = "Scissors"
        print("User choice is {}".format(ask_pick))

        print("Now it's the computer's turn....")
        import random
        computer_choice = random.randint(1, 3)
        if computer_choice == ROCK:
            computer_pick = "Rock"
        elif computer_choice == PAPER:
            computer_pick = "Paper"
        elif computer_choice == SCISSORS:
            computer_pick = "Scissors"
        print("Computer choice is: {}".format(computer_pick))

        print("{} V/S {}".format(ask_pick, computer_pick))
        if ask_choice == computer_choice:
            print("It is a tie.")
        elif ask_choice == ROCK and computer_choice == PAPER:
            print("{} wins =><== Computer wins ==>".format(computer_pick))
        elif ask_choice == PAPER and computer_choice == ROCK:
            print("{} wins =><== User wins ==>".format(ask_pick))
        elif ask_choice == ROCK and computer_choice == SCISSORS:
            print("{} wins =><== User wins ==>".format(computer_pick))
        elif ask_choice == SCISSORS and computer_choice == ROCK:
            print("{} wins =><== Computer wins ==>".format(ask_pick))
        elif ask_choice == PAPER and computer_choice == SCISSORS:
            print("{} wins =><== Computer wins ==>".format(computer_pick))
        elif ask_choice == SCISSORS and computer_choice == PAPER:
            print("{} wins =><== User wins ==>".format(ask_pick))

        redo = input("Do you want to play again? (Y/N)")
        if redo == "n" or redo == "N":
            print("Thank you for playing the game.\n"
                  "I had a great time.")
            quit()
RPS()
