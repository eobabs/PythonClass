import java.util.Scanner;

public class IncreasingOrder{

	public static void main(String... phasegate){

		Scanner input = new Scanner (System.in);
		
		System.out.print("\nEnter first number: ");
		int numberOne = input.nextInt();

		System.out.print("\nEnter second number: ");
		int numberTwo = input.nextInt();

		System.out.print("\nEnter third number: ");
		int numberThree = input.nextInt();
		

		

		if (numberTwo > numberOne && numberTwo > numberThree) {
			if (numberOne > numberThree) System.out.print("The numbers in increasing order " + numberThree + "," + numberOne + "," + numberTwo);
			else System.out.print("The numbers in increasing order " + numberOne + "," + numberThree  + "," + numberTwo);

			}

		if (numberOne > numberTwo && numberOne > numberThree) {
			if (numberTwo > numberThree) System.out.print("The numbers in increasing order " + "," + numberThree + numberTwo + "," + numberOne);
			else System.out.print("The numbers in increasing order " + numberTwo + "," + numberThree  + "," + numberOne);

			}

		if (numberThree > numberTwo && numberOne < numberThree) {
			if (numberTwo > numberOne) System.out.print("The numbers in increasing order " + numberOne + "," + numberTwo + "," + numberThree);
			else System.out.print("The numbers in increasing order " + numberTwo + "," + numberOne  + "," + numberThree);

			}


	}
}