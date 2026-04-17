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
			if (140.1 > h) {
				System.out.println(6);
			} else if (146 > h) {
				System.out.println(5);
			} else if (159 > h) {
				System.out.println(4);
			} else if (161 > h) {
				if (b >= 16.0 && b <= 35.0) {
					System.out.println(3);
				} else {
					System.out.println(4);
				}
			} else if (204 > h) {
				if (b >= 20.0 && b <= 25.0) {
					System.out.println(1);
				} else if ((b >= 18.5 && b <= 20.0) || (b >= 25.0 && b <= 30.0)) {
					System.out.println(2);
				} else if ((b >= 16.0 && b <= 18.5) || (b >= 30.0 && b <= 35.0)) {
					System.out.println(3);
				} else {
					System.out.println(4);
				}
			} else {
				System.out.println(4);
			}
		}
	}

	public static double getBmi(double height, double weight) {
		return weight/Math.pow(height/100, 2);
	}
}