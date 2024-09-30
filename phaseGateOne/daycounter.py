day_of_week_in_digits = int(input("""Enter current day
0 for Sunday
1 for Monday
2 for Tuesday
3 for Wednesday
4 for Thursday
5 for Friday
6 for Saturday
"""))
days_elapsed = int(input("Enter the number of days elapsed since today: "))

future_day = (day_of_week_in_digits + days_elapsed) % 7



print(f"Today is {days_elapsed} and the future day is {future_day}")

