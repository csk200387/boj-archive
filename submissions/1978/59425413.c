#include <stdio.h>

int main() {
	int a[100];
	int r = 0;
	int i, e;
	for (i = 0; i < 5; i++) {
		if (scanf("%d", &a[i]) != 1) exit(0);
	}
	for (i = 0; i < 5; i++) {
		e = 0;
		for (int j = 2; j < a[i] + 1; j++) {
			if (a[i] % j == 0) {
				e += 1;
				if (j == a[i] && e == 1) r += 1;
			}
		}
	}
	printf("%d", r);
	return 0;
}