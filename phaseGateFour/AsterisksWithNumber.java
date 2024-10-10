public class AsterisksWithNumber{

	public static void main(String args []){

		for (int count = 1; count <= 6; count++){
			System.out.println();
				
			for (int counter = 1; counter <= count; counter++){			
				if (counter % 2 == 0) {
					System.out.print("*");
				}
				else {
					System.out.print(counter); 
				}
			}
		}
	}
}