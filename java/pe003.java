

public class pe003 {

	public static void main (String[] argv) {
		long factor = 0L;
		long dividend = 2L;
		long n = 600851475143L;
	
		while (n > 1) {
			while (n%dividend == 0) {
				factor = dividend;
				n/= dividend;
			}
			dividend = dividend + 1;
			
			if (dividend*dividend > n) {
				if (n > 1) {
					factor = n;
				}
				break;
			}
		}
		System.out.println(factor);
	}
	
}