#include <stdio.h>
#include <stdlib.h>

int main() {
	int a, b;
	if (scanf("%d %d", &a, &b) != 2) exit(0);
	printf("%d\n", a*8+b*3-28);
}