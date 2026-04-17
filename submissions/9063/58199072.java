import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int size = input.nextInt();
		int x, y;
		int[] xArr = new int[size];
		int[] yArr = new int[size];
		
		for (int i = 0; i < size; i++) {
			x = input.nextInt();
			y = input.nextInt();
			xArr[i] = x;
			yArr[i] = y;
		}
		
		int result = (max(xArr)-min(xArr)) * (max(yArr)-min(yArr));
		
		System.out.println(result);
	}
	
	public static int min(int[] arr) {
		int res = arr[0];
		
		for (int i = 1; i < arr.length; i++) {
			if (arr[i] < res) res = arr[i];
		}
		return res;
	}
	public static int max(int[] arr) {
		int res = arr[0];
		
		for (int i = 1; i < arr.length; i++) {
			if (arr[i] > res) res = arr[i];
		}
		return res;
	}
}
