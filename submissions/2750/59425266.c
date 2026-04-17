#include <stdio.h>

int main() {
	int a[2001] = { 0, };

	int n;
	if (scanf("%d", &n) != 1) return 0;

	for (int i = 0; i < n; i++) {
		int x;
		if (scanf("%d", &x) != 1) return 0;
		a[x + 1000]++;
	}

	for (int i = 0; i < 2001; i++) {
		if (a[i] != 0) {
			printf("%d\n", i - 1000);
		}
	}
}