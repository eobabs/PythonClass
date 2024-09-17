'''
PSEUDOCODE

1. Keep requesting for user's deposit and store as a variable.
2. Keep requesting for user's withdrawals and store as a variable.
3. Get the sum of all deposits
4. Get the sum of all withdrawals
5. Find the difference between the sum and the withdrawals.
6. Store the difference as a variable.

'''
print("")

balance = 0

user_choice = int(input("Enter your choice: "))

while user_choice != 0:
	case 1 : 
		amount = float(input("Enter amount: "))
		balance += amount
	case 2 : 
		amount = float(input("Enter amount: "))
		if amount < balance :
			balance -= amount
		else :
			print ("Insufficient funds")

print (balance)

