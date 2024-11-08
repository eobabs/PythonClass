import random

def generate_random_numbers():
    return random.sample(range(1, 10), 3)  

def check_predictions(random_numbers, user_predictions):
    exact_matches = sum(1 for index in range(3) if random_numbers[index] == user_predictions[index])
    matches = len(set(random_numbers) & set(user_predictions))  

    if exact_matches == 3:
        return 5000  
    elif matches == 3:
        return 4000  
    elif matches == 2:
        return 3000  
    else:
        return 0 

def main():
    random_numbers = generate_random_numbers()
    print("Welcome to the number prediction game!")
    print("Please enter your predictions for three numbers (from 1 to 9) separated by spaces:")

    user_input = input("Your predictions: ")
    user_predictions = list(map(int, user_input.split()))

    if len(user_predictions) != 3 or any(num < 1 or num > 9 for num in user_predictions):
        print("Invalid input! Please enter exactly three numbers between 1 and 9.")
        return

    prize = check_predictions(random_numbers, user_predictions)

    print(f"Random numbers were: {random_numbers}")
    if prize > 0:
        print(f"Congratulations! You've won ${prize}!")
    else:
        print("Sorry, you didn't win this time.")

if __name__ == "__main__":
    main()
