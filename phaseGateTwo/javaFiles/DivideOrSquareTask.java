public class DivideOrSquareTask{

	public static void main(String... args){


		divideOrSquare(225);
		divideOrSquare(10);
		divideOrSquare(-225);
		

	}

	public static void divideOrSquare(int number){

		if (number < 0) System.out.println("Invalid. Enter a positive number");

		if (number % 5 == 0) System.out.printf("%.2f%n", Math.sqrt(number));
		else System.out.println(number % 5);
		
	}

}






