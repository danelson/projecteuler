import java.lang.Math;

public class pe007 {

	public int find_n_primes() {
		int[] primes = new int[10001];
		primes[0] = 2;
		primes[1] = 3;
		primes[10000] = 0;
		int current = 5;
		int index = 2;
		
		while (index < 10001) {
			int end = ((int)(Math.sqrt(current))) + 1;
			for (int i=2; i<end; i++) {
				if ((current%i) == 0 ) {
					break;
				}
				if (i == (int)(Math.sqrt(current))) {
					primes[index] = current;
					index++;
				}
			}
			current += 2;
		}
		return primes[10000];
	}
			

	public static void main (String[] argv) {
		pe007 test = new pe007();
		System.out.println(test.find_n_primes());
	}
	
}