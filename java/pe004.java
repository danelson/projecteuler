

public class pe004 {

	public static void main (String[] argv) {
		int value = 0;
		int a = 100;
		int b = 100;
		
		for (int i=100; i<999; i++) {
			for (int j=100; j<999; j++) {
				String strf = Integer.toString(i*j);
				String strb = new StringBuilder(strf).reverse().toString();
				if (strf.equals(strb) && i*j > value) {
					value = i*j;
				}
			}
		}
		System.out.println(value);
	}
	
}