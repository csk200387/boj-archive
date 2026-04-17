import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int K = sc.nextInt();
		int N = sc.nextInt();
		if (K == 1) {
			System.out.println(-1);
		} else {
			double v = (int) N*K/(N-1);
			double tmp = Math.ceil(v);
			if (N*K/(N-1) != 0) {
				tmp += 1.0;
			}
			System.out.println((int) tmp);
		}
		sc.close();
	}
}