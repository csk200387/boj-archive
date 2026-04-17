#include <stdio.h>
#include <math.h>

int sumstr(int t);

int main() {
	
	int n;
	int stack = 0;
	if (scanf("%d", &n) != 1) return 0;
	
	while (n > 9) {
		stack ++;
		n = sumstr(n);
	}
	
	printf("%d\n", stack);
	printf("%s\n", n%3==0 ? "YES" : "NO");
}

int sumstr(int t) {
	int sum = 0;
	int n;
	for (int i = 0; i < 7; i++) {
		n = (int)(t/pow(10, i)) % 10;
		sum += n;
	}
	return sum;
}