import java.util.Scanner;

public class Main {

	public static void Main(String[] args) {
		Scanner input = new Scanner(System.in);
		int num = input.nextInt();
		int i, t;
		for (i = 0; i < num; i++) {
			for (t = 0; t < num-1-i; t++) {
				System.out.print(" ");
			}
			for (t = 0; t < i*2+1; t++) {
				System.out.print("*");
			}
			System.out.println();
		}
		for (i = num-2; i >= 0; i--) {
			for (t = 0; t < num-1-i; t++) {
				System.out.print(" ");
			}
			for (t = 0; t < i*2+1; t++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}