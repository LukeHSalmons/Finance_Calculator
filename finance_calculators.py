import math

# User input whether calculate investment or bond
type = input('''Choose either 'investment' or 'bond' from the menu below to proceed:

investment   -   to calculate the amount of interest you'll earn on your investment
bond         -   to calculate the amount you'll have to pay on a home loan

''')
# Change input to lowercase
type = type.lower()

# Get all information from user if user enters investment
if type == 'investment':
    deposit = int(input("How much money are you depositing? "))
    interest_rate = int(input("What is the percentage of the interest rate? "))
    years = int(input("How many years are you planning on investing for? "))
    interest = input("Do you want to calculate 'compound' or 'simple' interest? ")
    interest_rate_divided = interest_rate / 100

    # Calculate and print simple interest
    if interest == "simple":
        total = deposit * (1 + interest_rate_divided * years)
        print(f"The total amount with simple interest applied is {total:.2f}")

    # Calculate and print compount interest
    elif interest == "compound":
        total = deposit * math.pow((1 + interest_rate_divided), years)
        print(f"The total amount with compound interest applied is {total:.2f}")
    else:
        print("You did not enter a valid interest type!")

# Get all information from user if user enters bond
elif type == 'bond':
    value = int(input("What is the current value of your house? "))
    interest_rate = int(input("What is the interest rate? "))
    time = int(input("How many months do you plan to repay the bond? "))
    interest_rate_monthly = (interest_rate / 12) / 100

    # Calculate and print monthly repayments
    repayment = (interest_rate_monthly * value) / (1 - (1 + interest_rate_monthly) ** (-time))
    print(f"You will need to pay {repayment:.2f} each month")

# Print message if user didn't enter a valid input when asked bond or investment
elif type == '':
    print("You did not enter anything")
else:
    print("You did not enter one of the above options!")