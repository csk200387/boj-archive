package ch4;

import java.util.Scanner;

class hihi {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int a, b, c;
		int[] arr = new int[3];
		while (true) {
			arr[0] = input.nextInt();
			arr[1] = input.nextInt();
			arr[2] = input.nextInt();
			if (sum(arr) == 0) {
				break;
			} else if (sum(arr) - max(arr) <= max(arr)) {
				System.out.println("Invalid");
			} else {
				if (arr[0] == arr[1] && arr[1] == arr[2] && arr[0] == arr[2]) {
					System.out.println("Equilateral");
				} else if (arr[0] == arr[1] || arr[1] == arr[2] || arr[0] == arr[2]) {
					System.out.println("Isosceles");
				} else {
					System.out.println("Scalene");
				}
			}
		}
	}
	private static int max(int[] arr) {
		int[] res = arr;
		
		for (int i = 0; i < res.length; i++) {
			if (res[0] < res[i]) res[0] = res[i];
		}
		return res[0];
	}
	private static int sum(int[] arr) {
		int res = 0;
		for (int i = 0; i < arr.length; i++) {
			res += arr[i];
		}
		return res;
	}
}
