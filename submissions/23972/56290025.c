#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int K, N;
	if (scanf("%d %d", &K, &N) == 1) {
		exit(1);
	} else {
		if (K == 1) {
			printf("-1\n");
		} else {
			double tmp = ceil(N*K/(N-1));
			if (N*K%(N-1)) tmp ++;
			printf("%d\n", (int) tmp);
		}
	}
}