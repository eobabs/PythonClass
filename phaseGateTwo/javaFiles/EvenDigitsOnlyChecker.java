public class EvenDigitsOnlyChecker{

	public static void main(String... args){

		int count = 0;

		for (int i = 1000; i <= 3000; i+=2){

			int unitDigit = i % 10;
			int tensDigit = (i / 10) % 10;
			int hundredsDigit = (i / 100) % 10;
			int thousandsDigit = (i / 1000);

		if (unitDigit % 2 == 0 && tensDigit % 2 == 0 && hundredsDigit % 2 == 0 && thousandsDigit % 2 == 0){

				count++;
				System.out.print(i + "," );
			
		}
	
			

		}

	}
}