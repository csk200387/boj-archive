import java.util.Scanner;

class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int h, w;
		double b;
		int n = sc.nextInt();
		
		for (int i = 0; i < n; i++) {
			h = sc.nextInt();
			w = sc.nextInt();
			b = getBmi(h, w);
			System.out.println(b);
			if (h >= 204) {
				System.out.println(4);
			} else if (h >= 161) {
				if (b >= 20.0 && b <= 25.0) {
					System.out.println(1);
				} else if ((b >= 18.5 && b <= 20.0) || (b >= 25.0 && b <= 30.0)) {
					System.out.println(2);
				} else if ((b >= 16.0 && b <= 18.5) || (b >= 30.0 && b <= 35.0)) {
					System.out.println(3);
				} else {
					System.out.println(4);
				}
			} else if (h >= 159) {
				if (b >= 16.0 && b <= 35.0) {
					System.out.println(3);
				} else {
					System.out.println(4);
				}
			} else if (h >= 146) {
				System.out.println(4);
			} else if (h >= 140.1) {
				System.out.println(5);
			} else {
				System.out.println(6);
			}
		}
	}

	public static double getBmi(double height, double weight) {
		return weight/Math.pow(height/100, 2);
	}
}