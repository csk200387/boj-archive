#include <stdio.h>
#include <stdlib.h>

int main() {
	int score = 0, tmp;
	for (int i = 0; i < 5; i++) {
		if (scanf("%d", &tmp) != 1) {
    		exit(1);
		}
		if (tmp > 40) {
			score += tmp;
		} else {
			score += 40;
		}
	}
	printf("%d", score / 5);
}