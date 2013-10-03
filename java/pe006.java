

public class pe006 {

	public int sum_of_squares(int n) {
		int sum = 0;
		for (int i=1; i<n+1; i++) {
			sum += i*i;
		}
		return sum;
	}

	public int square_of_sum(int n) {
		int sum = 0;
		for (int i=1; i<n+1; i++) {
			sum += i;
		}
		return sum*sum;
	}
	
	public static void main (String[] argv) {
		pe006 test = new pe006();
		System.out.println(test.square_of_sum(100) - test.sum_of_squares(100));
	}
	
}