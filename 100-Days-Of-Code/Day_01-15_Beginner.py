#--------------------------------------------- Day1: *bad* Band Name Generator ---------------------------------------------#

# Display non-suspicious text for false sense of security.
print("Welcome to the Band Name Generator!\n\n")

# Gather the user's city and pet name for future social engineering campaign.
city = input("What city did you grow up in?\n")
pet = input("What is the name of a pet?\n")

# Provide nonsense entertainment and store user information.
print(f"\nYour band name could be \"{city} {pet}\"\n\n")


# ----------------------------- Day2 Project: Tip Calculator -----------------------------

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
