import java.util.*;

public class ArrayOperations{

	public static void main (String... args){

		int [] numbers = new int [10];


		int count = 0;
		for (int index = 0; index < numbers.length; index++){
			numbers[index] =  1 + (int)(50 * Math.random());
			count++;
		}
			System.out.println("The length of the array is " + count);

		int sum = 0;
		

		for (int index = 0; index < numbers.length; index++){

			if (index % 2 == 0) 
			sum += numbers[index];
		} 
			System.out.println("The sum of the numbers in the even positions is " +sum);


		for (int index = 0; index < numbers.length; index++){

			if (index % 2 == 1) 
			sum += numbers[index];
		} 
			System.out.println("The sum of the numbers in the odd positions is " + sum);


		int product = 1;
		for (int index = 0; index < numbers.length; index++){

			if (index % 3 == 2) 
			product *= numbers[index];
		} 
			System.out.println("The product of the numbers at every third positions is " + product);

		for (int index = 0; index < numbers.length; index++){

			sum += numbers[index];
		} 

			System.out.println("The average of the numbers is " + sum/numbers.length);
	}

}