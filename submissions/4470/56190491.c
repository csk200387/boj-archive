#include <stdio.h>
#include <stdlib.h>

int main() {
	int num;
	char str[50];
	if (scanf("%d ", &num) != 1) {
		exit(1);
	}
	for (int i = 0; i < num; i++) {
		if (fgets(str, sizeof(str), stdin) == NULL) {
			exit(1);
		} else {
			printf("%d. %s", i+1, str);
		}
	}
}