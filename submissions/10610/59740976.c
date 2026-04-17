#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	char input[10001];
	int digits[10001] = {0};
	int len, sum = 0, i, j;

	if (fgets(input, sizeof(input), stdin) == NULL) exit(0);
	len = strlen(input) - 1;

	for (i = 0; i < len; i++) {
		digits[i] = input[i] - '0';
	}

	for (i = 0; i < len; i++) {
		if (digits[i] == 0) break;
		if (i == len - 1) {
			printf("-1\n");
			return 0;
		}
	}

	for (i = 0; i < len; i++) {
		for (j = i + 1; j < len; j++) {
			if (digits[i] < digits[j]) {
				int tmp = digits[i];
				digits[i] = digits[j];
				digits[j] = tmp;
			}
		}
	}

	for (i = 0; i < len; i++) {
		sum += digits[i];
	}
	if (sum % 3 != 0) {
		printf("-1\n");
		return 0;
	}

	for (i = 0; i < len; i++) {
		printf("%d", digits[i]);
	}
	printf("\n");

	return 0;
}