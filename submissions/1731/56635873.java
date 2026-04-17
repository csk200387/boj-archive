import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		int size = sc.nextInt();
		int[] arr = new int[size];
		int[] diff_a = new int[size-1]; // 등차수열
		int[] diff_g = new int[size-1]; // 등비수열
		for (int i = 0; i < size; i++) {
			arr[i] = sc.nextInt();
		}
		for (int i = 1; i < size; i++) {
			diff_a[i-1] = arr[i] - arr[i-1];
			diff_g[i-1] = arr[i] / arr[i-1];
		}
		if (check(diff_a)) {
			System.out.println(arr[size-1] + diff_a[size-2]);
		} else {
			System.out.println(arr[size-1] * diff_g[size-2]);
		}
		sc.close();
    }
	public static boolean check(int[] arr) {
		int ArraySize = arr.length;
		for (int i = 0; i < ArraySize/2; i++) {
			if (arr[i] != arr[ArraySize-i-1]) {
				return false;
			}
		}
		return true;
	}
}