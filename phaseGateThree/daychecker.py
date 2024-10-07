try: 
    day_of_week_checker = int(input("Enter day of the week (1-7): "))

    if day_of_week_checker < 1 or day_of_week_checker > 7:
        print("Invalid input. Please enter a number between 1 and 7.")
    else:
        day = { 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday" }
        print(f"Today is {day[day_of_week_checker]}")

except ValueError:
    print("Invalid input. Please enter a numeric value.")
