import java.util.Scanner;

public class CheckForSum {
  	public static void main(String[] args) {
        
     		Scanner userInput = new Scanner(System.in);
        
     	
     		int numberOne = (int)(100 * Math.random());
		int numberTwo = (int)(100 * Math.random());


		int sum = numberOne + numberTwo;

		System.out.printf("What is the sum of %d and %d?%n", numberOne, numberTwo);
     		int userAnswer = userInput.nextInt();

		if (userAnswer == sum) 	System.out.print("True");
		else System.out.print("False");

	}
}