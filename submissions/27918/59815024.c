#include <stdio.h>
#include <stdlib.h>
#define ABS(X) ((X)<0? -(X) : (X))
int main() {
	int n, d = 0, p = 0;
	char c;
	if (scanf("%d", &n) != 1) exit(0);
	for (int i = 0; i < n; i++) {
		if (scanf(" %c", &c) != 1) exit(0);
		if (c == 'D') d++;
		else if (c == 'P') p++;

		if (ABS(d-p) >= 2) {
			printf("%d:%d\n", d, p);
			exit(0);
		}
	}
	printf("%d:%d\n", d, p);
}