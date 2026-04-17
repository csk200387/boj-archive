import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String str = input.nextLine().trim();
		StringTokenizer st = new StringTokenizer(str, " ");
		System.out.println(st.countTokens());
	}
}