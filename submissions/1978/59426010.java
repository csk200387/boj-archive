import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int t, a, c = 0;
		for (int i = 0; i < n; i++) {
			t = sc.nextInt();
			if (t == 2) c++;
			else if (t > 0) {
				int j = 2;
				while (j < t) {
					if (t % j == 0) break;
					j++;
				}
				if (j == t) c++;
			}
		}
		sc.close();
		System.out.println(c);
	}
}