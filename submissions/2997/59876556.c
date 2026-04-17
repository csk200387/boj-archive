#include <stdio.h>

int main() {
	int a, b, c, t;
	if (scanf("%d %d %d", &a, &b, &c) != 3) return 0;
	if (b < a) {
		t = a;
		a = b;
		b = t;
	}
	if (c < a) {
		t = a;
		a = c;
		c = t;
	}
	if (c < b) {
		t = b;
		b = c;
		c = t;
	}
	if (b-a == c-b) printf("%d\n", c+c-b);
	else if (b-a > c-b) printf("%d\n", b+(b-c));
	else printf("%d\n", b+(b-a));
}