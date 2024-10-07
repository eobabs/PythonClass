def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"Deposited: ${amount:.2f}")
    else:
        print("Invalid deposit amount.")
    return balance

def withdraw(balance, amount):
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"Withdrew: ${amount:.2f}")
    else:
        print("Invalid withdrawal amount or insufficient funds.")
    return balance

def transfer(balance_from, balance_to, amount):
    if amount > 0 and amount <= balance_from:
        balance_from = withdraw(balance_from, amount)
        balance_to = deposit(balance_to, amount)
        print(f"Transferred: ${amount:.2f} to the second account")
    else:
        print("Invalid transfer amount or insufficient funds.")
    return balance_from, balance_to

balance1 = 0.0
balance2 = 0.0

while True:
    print("--- Bank Menu ---")
    print("1. Deposit (Account 1)")
    print("2. Withdraw (Account 1)")
    print("3. Transfer (Account 1 to Account 2)")
    print("4. Check Balance (Account 1)")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':  
        amount = float(input("Enter deposit amount: $"))
        balance1 = deposit(balance1, amount)

    elif choice == '2':
        amount = float(input("Enter withdrawal amount: $"))
        balance1 = withdraw(balance1, amount)

    elif choice == '3': 
        amount = float(input("Enter transfer amount: $"))
        balance1, balance2 = transfer(balance1, balance2, amount)

    elif choice == '4':  
        print(f"Current balance (Account 1): ${balance1:.2f}")

    elif choice == '5':  
        print("Exit the application")
        break

    else:
        print("Invalid option. Please try again.")
