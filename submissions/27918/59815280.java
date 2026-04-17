import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int d = 0, p = 0;
		int n = sc.nextInt();

		for (int i = 0; i < n; i++) {
			String c = sc.next();
			if (c.equals("D")) {
				d++;
			} else {
				p++;
			}

			if (Math.abs(d - p) >= 2) {
				System.out.println(d + ":" + p);
				System.exit(0);
			}
		}
		System.out.println(d + ":" + p);
	}
}