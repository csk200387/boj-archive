#include <stdio.h>

int main() {
	int a[101];
	int n, c = 0;
	if (scanf("%d", &n) != 1) return 0;

	for (int i = 0; i < n; i++) {
		if (scanf("%d", &a[i]) != 1) return 0;
		// find prime number
		if (a[i] == 2) c++;
		else if (a[i] > 2) {
			int j = 2;
			while (j < a[i]) {
				if (a[i] % j == 0) break;
				j++;
			}
			if (j == a[i]) c++;
		}
	}
	printf("%d\n", c);
}