#include <stdio.h>

int main() {
	int t, n, c = 0;
	if (scanf("%d", &n) != 1) return 0;

	for (int i = 0; i < n; i++) {
		if (scanf("%d", &t) != 1) return 0;
		if (t == 2) c++;
		else if (t > 2) {
			int j = 2;
			while (j < t) {
				if (t % j == 0) break;
				j++;
			}
			if (j == t) c++;
		}
	}
	printf("%d\n", c);
}