'''
PSEUDOCODE

1. Keep requesting for user's deposit and store as a variable.
2. Keep requesting for user's withdrawals and store as a variable.
3. Get the sum of all deposits
4. Get the sum of all withdrawals
5. Find the difference between the sum and the withdrawls.
6. Store the difference as a variable.

'''

print("")
number_of_deposits = int(input("Enter number of deposits: "))

sum_of_deposits = 0 
count = 1
while (count <= number_of_deposits):

	value_of_deposit = float(input("Enter the amount you want to deposit: $"))
	sum_of_deposits += value_of_deposit
	count +=1

print("")
number_of_withdrawals = int(input("Enter number of withdrawals: "))

sum_of_withdrawals = 0
count = 1
while (count <= number_of_withdrawals):
	
	if sum_of_deposits > 0 :
		value_of_withdrawals = float(input("Enter the amount you want to withdraw: $"))
		sum_of_withdrawals += value_of_withdrawals
	if sum_of_deposits <= 0 :
		print ("You do not have sufficient amount to withdraw")
	count +=1

print("")
if sum_of_deposits >= sum_of_withdrawals :

	balance = sum_of_deposits - sum_of_withdrawals
	print ("The user's balance is: $", balance)

else : 
	print ("Insufficient Funds")