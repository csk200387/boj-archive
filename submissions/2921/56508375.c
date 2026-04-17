#include <stdio.h>
#include <stdlib.h>

int main() {
	int n;
	if (scanf("%d", &n) != 1) {
		exit(1);
	} else {
		int result = 0;
		for (int i = 0; i <= n; i++) {
			for (int l = i; l <= n; l++) {
				result += i + l;
			}
		}
		printf("%d\n", result);
	}
}