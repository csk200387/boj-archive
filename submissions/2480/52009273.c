#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	int d1, d2, d3;
	scanf("%d %d %d", &d1, &d2, &d3);
	if (d1 == d2 && d2 == d3 && d3 == d1) {
		printf("%d\n", 10000 + d1 * 1000);
		return 0;
	}
	else if (d1 == d2 || d3 == d1) {
		printf("%d\n", 1000 + d1 * 100);
		return 0;
	}
	else if (d2 == d3) {
		printf("%d\n", 1000 + d2 * 100);
		return 0;
	}
	else {
		if (d1 > d2 && d1 > d3)
			printf("%d\n", d1*100);
		else if (d2 > d1 && d2 > d3)
			printf("%d\n", d2*100);
		else
			printf("%d\n", d3*100);
	}
}