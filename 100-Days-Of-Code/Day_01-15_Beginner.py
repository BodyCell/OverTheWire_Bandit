#--------------------------------------------- Day1: *bad* Band Name Generator ---------------------------------------------#

def BandNameGenerator(city,pet):
    # Display non-suspicious text for false sense of security.
    print("Welcome to the Band Name Generator!\n\n")

    # Gather the user's city and pet name for future social engineering campaign.
    city = input("What city did you grow up in?\n")
    pet = input("What is the name of a pet?\n")

    # Provide nonsense entertainment and store user information.
    print(f"\nYour band name could be \"{city} {pet}\"\n\n")


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

traffic_game()