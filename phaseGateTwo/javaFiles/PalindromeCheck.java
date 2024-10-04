public class PalindromeCheck{

	public static void main(String... args){

		PalindromeCheck check = new PalindromeCheck();

		System.out.print(check.isPalindrome(4204));

	}

	public boolean isPalindrome(int number){

		return number == reverse(number);
	
	}

	public int reverse(int number){

		int reversedNumber = 0;

		while (number != 0){
			reversedNumber = (reversedNumber * 10) + number % 10;
			number /= 10;
		}

		return reversedNumber;
	}
}