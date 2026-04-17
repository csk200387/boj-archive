#include <stdio.h>

void swap(short *a, short *b) {
	short t = *a;
	*a = *b;
	*b = t;
}

int main() {
	short a, b, c;
	if (scanf("%hd %hd %hd", &a, &b, &c) != 3) return 0;
	if (a > b) swap(&a, &b);
	if (b > c) swap(&b, &c);
	if (a > b) swap(&a, &b);
	if (b-a == c-b) printf("%d\n", c+c-b);
	else if (b-a > c-b) printf("%d\n", b+(b-c));
	else printf("%d\n", b+(b-a));
}