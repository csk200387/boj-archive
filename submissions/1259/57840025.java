import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String data, result;
		while (true) {
			data = input.next();
			if (data == "0") {
				break;
			} else {
				result = isPalindrome(data) ? "yes" : "no";
				System.out.println(result);
			}
		}
	}
	private static boolean isPalindrome(String data) {
		int len = data.length();
		int tr = len/2;
		for (int i = 0; i < tr; i++) {
			if (data.charAt(i) != data.charAt(len-i-1)) {
				return false;
			}
		}
		return true;
	}
}