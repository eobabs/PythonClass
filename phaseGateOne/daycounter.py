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


day = { 

	0 : "Sunday",
	1 : "Monday",
	2 : "Tuesday",
	3 : "Wednesday",
	4 : "Thursday",
	5 : "Friday",
	6 : "Saturday"
	}
	
	



print(f"Today is {day[day_of_week_in_digits]} and the future day is {day[future_day]}")

