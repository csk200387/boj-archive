import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int index = 1;
		for (int i = 1; i <= N; i++) {
			if (N % i == 0) {
				if (index == M) {
					System.out.println(i);
					System.exit(0);
				} else if (index > M) {
					break;
				}
				index ++;
			}
		}
		System.out.println(0);
	}
}