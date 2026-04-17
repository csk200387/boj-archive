#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	int num, money;
	int res = 0;
	scanf("%d", &money);
	scanf("%d", &num);
	for (int i = 0; i < num; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		res = res + a * b;
	}
	if (res == money) {
		printf("Yes");
	}
	else {
		printf("No");
	}
}