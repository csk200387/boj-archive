#include <stdio.h>
#include <stdlib.h>

int main() {
	int N, M, index = 0;
	int arr[1000] = { 0, };
	if (scanf("%d %d", &N, &M) == 1) {
		exit(1);
	} else {
		for (int i = 1; i <= N; i++) {
			if (N % i == 0) {
				arr[index] += i;
				index ++;
			}
		}
		printf("%d\n", arr[M-1]);
	}
}