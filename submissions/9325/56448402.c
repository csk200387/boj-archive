#include <stdio.h>
#include <stdlib.h>

int main() {
	int cs;
	if (scanf("%d", &cs) != 1) {
		exit(1);
	} else {
		for (int i = 0; i < cs; i++) {
			int result, n, a, b;
			if (scanf("%d", &result) != 1) exit(0);
			if (scanf("%d", &n) != 1) exit(0);
			for (int j = 0; j < n; j++) {
				if (scanf("%d %d", &a, &b) != 2) exit(0);
				result += a*b;
			}
			printf("%d\n", result);
		}
	}
}