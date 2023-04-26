def check_balance():
    # Get balance from user account
    balance = 50000
    # Display balance to user
    print("Your current balance is:", balance)

def withdraw(amount):
    # Get balance from user account
    balance = 50000
    # Check if withdrawal amount is greater than balance
    if amount > balance:
        print("Insufficient funds")
    else:
        # Subtract withdrawal amount from balance
        balance -= amount
        # Display remaining balance to user
        print("Your remaining balance is:-->", balance,"your withdraw amount is:-->",amount)

def deposit(amount):
    # Get balance from user account
    balance = 50000
    # Add deposit amount to balance
    balance += amount
    # Display updated balance to user
    print("Your updated balance is:", balance)


# Display options to the user
print("Select operation:")
print("-->click the '1' number for check balance: ")
print("-->click the '-' symbol for    Withdraw:")
print("->click the '+' symbol for Deposit:")

# Get user input for choice of operation
choice = input("Enter choice (1/-/+): ")

# Perform selected operation based on user input
if choice == '1':
    check_balance()

elif choice == '-':
    # Get user input for withdrawal amount
    amount = float(input("Enter withdrawal amount: "))
    withdraw(amount)

elif choice == '+':
    # Get user input for deposit amount
    amount = float(input("Enter deposit amount: "))
    deposit(amount)

else:
    print("Invalid input")
