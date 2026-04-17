import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int r = 0;
		n = n % 8;

		if (n == 1) r = 1;
		else if (n == 2 || n == 0) r = 2;
		else if (n == 3 || n == 7) r = 3;
		else if (n == 4 || n == 6) r = 4;	
		else if (n == 5) r = 5;
		System.out.println(r);
	}
}