

public class pe002 {

	public static void main (String[] argv) {
		int prev = 0;
		int curr = 1;
		int next;
		int value = 0;
	
		while (curr < 4000000) {
			next = prev + curr;
			prev = curr;
			curr = next;
			if (curr%2 == 0) {
				value += curr;
			}
		}
	
		System.out.println(value);
	}
	
}