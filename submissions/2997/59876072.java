import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
		int t;
        sc.close();
		if (b < a) {
			t = b;
			b = a;
			a = t;
		}
		if (c < a) {
			t = c;
			c = b;
			b = t;
		}
		if (c < b) {
			t = b;
			b = c;
			c = t;
		}
        if (b-a == c-b) System.out.println(c+c-b);
        else if (b-a > c-b) System.out.println(b + (b - c));
        else System.out.println(b + (b - a));
    }
}