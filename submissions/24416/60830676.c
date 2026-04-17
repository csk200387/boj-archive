#include <stdio.h>

int main() {
	int n;
	if (scanf("%d", &n) != 1) return 1;
	int f[n];
	f[0] = 1;
	f[1] = 1;
	for (int i = 2; i < n; i++) {
		f[i] = f[i-1] + f[i-2];
	}
	printf("%d %d\n", f[n-1], n-2);
	return 0;
}