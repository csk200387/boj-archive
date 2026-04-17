#include <stdio.h>
#include <stdlib.h>

int main() {
	int n, m;
	float C, G;
	if (scanf("%d", &n) != 1) exit(0);
	for (int i = 0; i < n; i++) {
		C = 0, G = 0, m = 0;
		if (scanf("%d", &m) != 1) exit(0);
		for (int l = 0; l < m; l++) {
			float A, B;
			if (scanf("%f %f", &A, &B) != 2) exit(0);
			C += A;
			G += A*B;
		}
		printf("%d %.1f\n", (int) C, G/C);
	}
}