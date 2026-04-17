#include <stdio.h>
#include <stdlib.h>

int main() {
	int N, M, index = 1;
	if (scanf("%d %d", &N, &M) == 1) {
		exit(1);
	} else {
		for (int i = 1; i <= N; i++) {
			if (N % i == 0) {
				if (index == M) {
					printf("%d", i);
					exit(0);
				} else if (index > M) {
					printf("0");
					exit(0);
				}
				index ++;
			}
		}
	}
	printf("0");
}