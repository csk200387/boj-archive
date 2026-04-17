import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int size = sc.nextInt();
		int c = sc.nextInt();
		int[] arr = new int[size];
		for (int i = 0; i < size; i++) {
			arr[i] = sc.nextInt();
		}
		System.out.println(func(arr, size, c));
	}
	private static int func(int[] arr, int size, int n) {
		for (int i = 0; i < n; i++) {
			int min = i;
			for (int j = i + 1; j < size; j++) {
				if (arr[j] >= arr[min]) {
					min = j;
				}
			}
			int temp = arr[i];
			arr[i] = arr[min];
			arr[min] = temp;
		}
		return arr[n-1];
	}
}