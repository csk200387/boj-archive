import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int[] arr = new int[1000001];
		Scanner sc = new Scanner(System.in);
		int size = sc.nextInt();
		int index;
		for (int i = 0; i < size; i++) {
			index = sc.nextInt();
			arr[index]++;
		}
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] != 0) {
				System.out.println(i);
			}
		}
	}
}