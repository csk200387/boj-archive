import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String str = input.nextLine();
		String[] spl = str.split(" ");
		System.out.println(spl.length);
	}
}