import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		int coupon = sc.nextInt();
		int price = sc.nextInt();
		int[] arr = { price-500, (int)(price*0.9), price-2000, (int)(price*0.75) };
		int result = price;
		for (int i = 0; i <= coupon/5; i++) {
			if (result > arr[i]) {
				result = arr[i];
			}
		}
		if (result < 0) {
			result = 0;
		}
		sc.close();
		System.out.println(result);
    }
}