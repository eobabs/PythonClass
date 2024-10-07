def get_total_deposits():
    number_of_deposits = int(input("Enter number of deposits: "))
    total_deposits = 0
    for _ in range(number_of_deposits):
        value_of_deposit = int(input("Enter the amount you want to deposit: $"))
        total_deposits += value_of_deposit
    return total_deposits

def get_total_withdrawals(total_deposits):
    number_of_withdrawals = int(input("Enter number of withdrawals: "))
    total_withdrawals = 0
    for _ in range(number_of_withdrawals):
        if total_deposits > 0:
            value_of_withdrawal = int(input("Enter the amount you want to withdraw: $"))
            if value_of_withdrawal <= total_deposits:
                total_withdrawals += value_of_withdrawal
                total_deposits -= value_of_withdrawal
            else:
                print("You do not have sufficient amount to withdraw")
                break
        else:
            print("No funds available for withdrawal")
            break
    return total_withdrawals

def calculate_balance(total_deposits, total_withdrawals):
    if total_deposits >= total_withdrawals:
        return total_deposits - total_withdrawals
    else:
        print("Insufficient Funds")
        return None

def main():
    total_deposits = get_total_deposits()
    total_withdrawals = get_total_withdrawals(total_deposits)
    balance = calculate_balance(total_deposits, total_withdrawals)
    
    if balance is not None:
        print(f"The user's balance is: ${balance}")

if __name__ == "__main__":
    main()
