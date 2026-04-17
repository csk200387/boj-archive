#include <stdio.h>

int main() {
	int num;
	char str[50];
	scanf("%d ", &num);
	for (int i = 0; i < num; i++) {
		gets(str);
		printf("%d. %s\n", i+1, str);
	}
}