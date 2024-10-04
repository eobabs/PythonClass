import java.util.*;

public class IntegerToString{

	public static void main(String... args){

	format (23,9);

	}	

	public static String format(int numberOne, int numberTwo){
	
		String text = "";

		int sum = numberOne + numberTwo;

		text += sum;
		
		System.out.print(text);

		return text;
	}

}

