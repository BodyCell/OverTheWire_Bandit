# memail mfybylbobwicbnakpn@bbitq.com #
#--------------------------------------------- Day1: *bad* Band Name Generator ---------------------------------------------#

def BandNameGenerator(city,pet):
    # Display non-suspicious text for false sense of security.
    print("Welcome to the Band Name Generator!\n\n")

    # Gather the user's city and pet name for future social engineering campaign.
    city = input("What city did you grow up in?\n")
    pet = input("What is the name of a pet?\n")

    # Provide nonsense entertainment and store user information.
    print(f"\nYour band name could be \"{city} {pet}\"\n\n")

# BandNameGenerator()

#----------------------------- Day2 Project: Tip Calculator -----------------------------#

def TipCalculator(total_bill,customers,tip_percent):
    # Display non-suspicious text for false sense of security.
    print("Welcome to the Tip Calculator!\n")

    # Gather abstract understanding of target's spending habits.
    total_bill = float(input("\nWhat was the total bill?\n$"))

    # Receive number of potential targets for future attacks.
    customers = int(input("\nHow many people are going to split the bill?\n"))

    # Gather an understanding of how cheap
    tip_percent = int(input("\nWhat percentage tip would you like to give? (e.g. 10, 12, 15, 20)\n"))

    # Provide nonsense output and store user information.
    print(f"Each person should contribue: ${(total_bill*((tip_percent*.01)+1))/customers}\n\n")

#TipCalculator()


#----------------------------- Day3 Project: Traffic Game -----------------------------#

# trip = 30
def traffic_game():
    trip = 30

    def fast_lane():
        print("\nYou passed up the garbage truck. Your trip has been shortened by 3 minutes!\n")
        
    def slow_lane():
        print("\nBummer, you got behind a student driver. Your trip has been incresed by 5 minutes..\n")
        
    def no_diff():
        print("\nAll lanes are just going slow right now... Your trip time has not changed.\n")

    def wreck():
        print("\nWoowww, there's a wreck on the highway! Your trip time has been incresed by 15 minutes!\n")
        
    def speeding():
        print("\nYou decide to go 60 in a 20 (you little dare devil). Your trip time has decresed by 20 minutes!\n")
        

    print("\n\nIt's 8:30 and you finally made it out of the house. The office is 30 mintues away (no more work from home 😪)\n")

    if(input("\nYou hit a school zone.. Will you obey the speed limit?\n(Y/N): ").lower()=="n"):
        speeding()
        trip -=20
        if(input("\nYou come to a stop light. There are 3 cars in front of you, but only one car in the lane next to you.\nWill you switch lanes?\n(Y/N): ").lower()=="y"):
            slow_lane()
            trip+=5
        else:print("Congratulations, you made it to work for another day!🥳")
    else:
        print("\nThere is no way you will make it to work on time. YOU'RE FIRED!!!\n")

# traffic_game()


#----------------------------- Day4 Project: Rock, Paper, Scissors -----------------------------#

def rock_paper_scissors():
    import random

    options = ("Rock","Paper","Scissors")

    comp_choice = options[random.randint(0,2)].lower()

    player_choice = input("Choose rock, paper, or scissors.\n").lower()

    print("\nComputer chose", comp_choice+"...")

    def player_lost():
        return ((player_choice.startswith("r") and comp_choice.startswith("p")) 
                or (player_choice.startswith("p") and comp_choice.startswith("s")) 
                or (player_choice.startswith("s") and comp_choice.startswith("r")))

    def player_won():
        return ((comp_choice.startswith("r") and player_choice.startswith("p")) 
                or (comp_choice.startswith("p") and player_choice.startswith("s")) 
                or (comp_choice.startswith("s") and player_choice.startswith("r")))

    def player_tie():
        return ((comp_choice.startswith("r") and player_choice.startswith("r")) 
            or (comp_choice.startswith("p") and player_choice.startswith("p")) 
            or (comp_choice.startswith("s") and player_choice.startswith("s")))


    if player_lost():
        print("sOrRy, YoU lOsT!")

    elif player_won():
        print("Hey... you won!")

    elif player_tie():
        print("Tie game.")

    else:
        print("You didn't make a valid choice")

# rock_paper_scissors()

#----------------------------- Day5 Project: Password Generator -----------------------------#

def PasswordGenerator():
    import random


    auto_length = "16"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = lower_letters.upper()
    numbers = "0123456789"
    symbols = "!@#$%^&*,."
    all_characters = lower_letters+upper_letters+numbers+symbols


    print("Welcome to the Password Generator\n\n")

    user_choice = input("Enter a '1' for an auto-generated password ("+auto_length+" characters).\nEnter a '2' to customize your generated password.\n\n")
    pass_array = []


    if user_choice=='1':
        for x in range(int(auto_length)):
            pass_array.append(all_characters[random.randint(0,len(all_characters)-1)])

    elif user_choice=='2':
        num_lower_letters = int(input("How many lower case letters would you like?\n"))
        for x in range(num_lower_letters):
            pass_array.append(lower_letters[random.randint(0,len(lower_letters)-1)])
        
        num_upper_letters = int(input("How many upper case letters would you like?\n"))
        for x in range(num_upper_letters):
            pass_array.append(upper_letters[random.randint(0,len(upper_letters)-1)])
 
        num_numbers = int(input("How many numbers would you like?\n"))
        for x in range(num_numbers):
            pass_array.append(numbers[random.randint(0,len(numbers)-1)])

        num_symbols = int(input("How many symbols would you like?\n"))
        for x in range(num_symbols):
            pass_array.append(symbols[random.randint(0,len(symbols)-1)])
        
        random.shuffle(pass_array)

    else:
        print("That is not a valid choice my friend...")
        exit()


    user_pass = ""
    for x in pass_array:
        user_pass+=x
    print("Your generated password is: '"+user_pass+"'")


# PasswordGenerator()

#----------------------------- Day6 Project: Reeborg Maze -----------------------------#
#URL to maze: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if wall_on_right():
#         if front_is_clear():
#             move()
#         else:
#             turn_left()
#     else:
#         turn_right()
#         move()
