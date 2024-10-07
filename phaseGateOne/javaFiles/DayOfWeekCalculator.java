import java.util.Scanner;

public class DayOfWeekCalculator {
	public static void main(String[] args) {
        	Scanner dayCounter = new Scanner(System.in);

        	System.out.println("Enter current day");
        	System.out.println("0 for Sunday");
        	System.out.println("1 for Monday");
       		System.out.println("2 for Tuesday");
        	System.out.println("3 for Wednesday");
        	System.out.println("4 for Thursday");
        	System.out.println("5 for Friday");
        	System.out.println("6 for Saturday");
        
		int dayOfWeekInDigits = dayCounter.nextInt();

        	System.out.print("Enter the number of days elapsed since today: ");
        	int daysElapsed = dayCounter.nextInt();

        	int futureDay = (dayOfWeekInDigits + daysElapsed) % 7;

        	String[] days = { "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" };

        System.out.printf("Today is %s and the future day is %s%n", days[dayOfWeekInDigits], days[futureDay]);


    }
}
