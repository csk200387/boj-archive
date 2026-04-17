#include <stdio.h>
#include <stdlib.h>

int main() {
	int score = 0, tmp, i;
	int arr[30] = { 0, };
	for (i = 0; i < 28; i++) {
		if (scanf("%d", &tmp) != 1) {
			exit(1);
		}
		arr[tmp-1] ++;
	}
	for (i = 0; i < 30; i++) {
		if (arr[i] == 0) {
			printf("%d\n", i+1);
		}
	}
}