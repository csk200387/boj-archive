#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	long long int K, N;
	if (scanf("%lld %lld", &K, &N) == 1) {
		exit(1);
	} else {
		if (K == 1) {
			printf("-1\n");
		} else {
			long long int tmp = ceil((double) N*K/(N-1));
			if ((N*K) % (N-1) != 0) tmp ++;
			printf("%lld\n", tmp);
		}
	}
}