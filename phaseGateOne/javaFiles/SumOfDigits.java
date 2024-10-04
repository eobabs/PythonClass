import java.util.Scanner;

public class SumOfDigits {

	public static void main(String[] args) {
        	Scanner inputCollector = new Scanner(System.in);
        
       		System.out.print("Enter a number between 0 and 1000(both inclusive): ");
        	int number = inputCollector.nextInt();
        
		int numberToCheck = number;
		int sumOfDigits = 0;
		
		while (numberToCheck != 0){
			extractedDigit = numberToCheck % 10
			sumOfDigits = sumOfDigits + extractedDigit
			numberToCheck //= 10
		}
	
		System.out.printf("The sum of all the digits of %d is %d ", number, sumOfDigits )


        
    }
}
