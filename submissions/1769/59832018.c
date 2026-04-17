#include <stdio.h>
#include <math.h>

int sumstr(int t);

int main() {
	int n;
	int stack = 0;
	if (scanf("%d", &n) != 1) return 0;
	
	do {
		stack ++;
		n = sumstr(n);
	} while (n > 9);
	
	printf("%d\n", stack);
	printf("%s\n", n%3>0 ? "NO" : "YES");
}

int sumstr(int t) {
	int sum = 0;
	int n;
	for (int i = 0; i < 10; i++) {
		n = (int)(t/pow(10, i)) % 10;
		if (n == 0) break;
		sum += n;
	}
	return sum;
}