import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i = 2;
		String s;
		while (true) {
			s = sc.nextLine();
			if (s.equals("Was it a cat I saw?")) break;
			for (int j = 0; j < s.length(); j += i) {
				System.out.print(s.charAt(j));
			}
			System.out.println();
			i++;
		}		
	}
}