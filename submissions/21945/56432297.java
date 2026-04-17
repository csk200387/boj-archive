import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		long result = 0;
        int n = sc.nextInt();
		sc.nextLine();
        String input = sc.nextLine();
		String[] arr = input.split(" ");

		for (int i = 0; i < n; i++) {
			if (isPalindrome(arr[i])) {
				result += Integer.parseInt(arr[i]);
			}
		}
		System.out.println(result);
		sc.close();
    }
	public static boolean isPalindrome(String str) {
		int i = 0, j = str.length() - 1;
		while (i < j) {
			if (str.charAt(i) != str.charAt(j)) {
				return false;
			}
			i++;
			j--;
		}
		return true;
	}
}