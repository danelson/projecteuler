

public class pe005 {
	/*
	public int multiple() {
		int value = 2520;
		
		while (true) {
			int answer = loop(value);
			if (answer != -1) {
				return answer;
			}
			value += 2520;
		}
	}

	public int loop(int value) {
		for (int i=2; i<21; i++) {
			if (value%i != 0) {
				return -1;
			}
			if (i == 20) {
				return value;
			}
		}
		return -1;
	}
	*/
	
	public int multiple() {
		int value = 2520;
		while (true) {
			for (int i=2; i<21; i++) {
				if ((value % i) != 0) {
					break;
				}
				if (i == 20) {
					return value;
				}
			}
			value += 2520;
		}
	}
	
	public static void main (String[] argv) {
		pe005 test = new pe005();
		System.out.println(test.multiple());
	}
}