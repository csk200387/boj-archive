#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	int h, m, inpm;
	scanf("%d %d", &h, &m);
	scanf("%d", &inpm);
	m = m + inpm;
	if (m > 60) {
		h = h + m / 60;
		m = m % 60;
	}
	if (h > 24) {
		h = h % 24;
	}
	printf("%d %d", h, m);
}