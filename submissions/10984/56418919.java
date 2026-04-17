import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for (int i = 0; i < n; i++) {
			float C = 0, G = 0;
			int m = sc.nextInt();
			for (int j = 0; j < m; j++) {
				float A = sc.nextFloat();
				float B = sc.nextFloat();
				C += A;
				G += A*B;
			}
			String result = String.format("%d %.1f", (int) C, G/C);
			System.out.println(result);
		}
		sc.close();
	}
}