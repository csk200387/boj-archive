import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		int cs = sc.nextInt();
		for (int i = 0; i < cs; i++) {
			int result = sc.nextInt();
			int n = sc.nextInt();
			for (int j = 0; j < n; j++) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				result += a*b;
			}
			System.out.println(result);
		}
		sc.close();
    }
}