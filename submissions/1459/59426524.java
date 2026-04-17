import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long case1, case2, case3;
		long x = sc.nextLong();
		long y = sc.nextLong();
		int w = sc.nextInt();
		int s = sc.nextInt();
		
		case1 = (x+y) * w;

		if ((x+y) % 2 == 0) {
			if (x > y) case2 = x*s;
			else case2 = y*s;
		}
		else {
			if (x > y) case2 = (x-1)*s + w;
			else case2 = (y-1)*s + w;
		}

		if (x > y) case3 = y*s + (x-y)*w;
		else case3 = x*s + (y-x)*w;

		if (case1 < case2 && case1 < case3) System.out.println(case1);
		else if (case2 < case1 && case2 < case3) System.out.println(case2);
		else System.out.println(case3);
		
		sc.close();
	}
}