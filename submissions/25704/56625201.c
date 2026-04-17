#include <stdio.h>
#include <stdlib.h>

int main() {
	int coupon, price;
	if (scanf("%d", &coupon) != 1) exit(0);	
	if (scanf("%d", &price) != 1) exit(0);	
	int arr[6] = { price-500, (int)(price*0.9), price-2000, (int)(price*0.75), price, price };
	int result = price;
	for (int i = 0; i < coupon/5; i++) {
		if (result > arr[i]) {
			result = arr[i];
		}
	}
	if (result < 0) {
		result = 0;
	}
	printf("%d\n", result);
}