'''
PSEUDOCODE

1. Keep requesting for user's deposit and store as a variable.
2. Keep requesting for user's withdrawals and store as a variable.
3. Get the sum of all deposits
4. Get the sum of all withdrawls
5. Find the difference between the sum and the withdrawls.
6. Store the difference as a variable.

'''
print("")
number_of_deposits = int(input("Enter number of deposits: "))

total_deposits = 0 
for count in range (number_of_deposits):
	value_of_deposit = int(input("Enter the amount you want to deposit: $"))
	total_deposits += value_of_deposit

print("")
number_of_withdrawals = int(input("Enter number of withdrawals: "))

total_withdrawals = 0
for count in range (number_of_withdrawals):
	if total_deposits > 0 :
		value_of_withdrawals = int(input("Enter the amount you want to withdraw: $"))
		total_withdrawals += value_of_withdrawals
	else :
		print ("You do not have sufficient amount to withdraw")
		break

print("")
if total_deposits > total_withdrawals :

	balance = total_deposits - total_withdrawals
	print ("The user's balance is: $", balance)

else : 
	print ("Insufficient Funds")