#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	char *str = (char *)malloc(sizeof(char) * 1000000);
	int count = 0;

	if (scanf("%[^\n]s", str) != 1) return 0;

	for (int i = 0; i < strlen(str); i++) {
		if (str[i] == ' ') count++;
	}

	if (str[0] == ' ') count--;
	if (str[strlen(str) - 1] == ' ') count--;

	printf("%d\n", count + 1);

	free(str);

	return 0;
}