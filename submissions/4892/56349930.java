import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n0, n1, n2, n3, n4;
		String res = "";
		for (int stack = 1; true; stack++) {
			n0 = sc.nextInt();
			if (n0 == 0) {
				break;
			} else {
				n1 = n0*3;
				if ((n1 & 1) == 0) {
					n2 = n1/2;
					res = "even";
				} else {
					n2 = (n1+1)/2;
					res = "odd";
				}
				n3 = n2*3;
				n4 = n3/9;
				String message = String.format("%d. %s %d", stack, res, n4);
				System.out.println(message);
			}
		}

		sc.close();
	}
}