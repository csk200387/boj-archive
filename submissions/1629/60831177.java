import java.util.Scanner;

public class Main {
	long A, B, C;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Main obj = new Main();
		obj.A = sc.nextLong();
		obj.B = sc.nextLong();
		obj.C = sc.nextLong();
		System.out.println(obj.prob(obj.B));
		sc.close();
	}

	public long prob(long n) {
		if (n == 1) return A % C;
		if (n % 2 == 0) {
			long a = prob(n / 2);
			return a * a % C;
		} else {
			long a = prob(n / 2);
			return ((a * a) % C * A) % C;
		} 

	}
}