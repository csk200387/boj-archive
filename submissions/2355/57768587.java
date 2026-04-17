import java.util.Scanner;

public class Main {
    
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		long n = input.nextInt();
		long m = input.nextInt();
		long a = Math.max(n, m);
		long b = Math.min(n, m);
		System.out.println((n+m)*(a-b+1)/2);
	}
}