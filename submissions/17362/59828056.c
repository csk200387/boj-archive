#include <stdio.h>

int main() {
	int n;
	if (scanf("%d", &n) != 1) exit(0);
	n = n%8;
	if (n == 1) printf("1");
	else if (n == 2 || n == 0) printf("2\n");
	else if (n == 3 || n == 7) printf("3\n");
	else if (n == 4 || n == 6) printf("4\n");
	else printf("5\n");
}