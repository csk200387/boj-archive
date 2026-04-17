#include <stdio.h>

int main() {
	long long int x, y, case1, case2, case3;
	int w, s;
	if (scanf("%lld %lld %d %d", &x, &y, &w, &s) != 4) return 0;
	
	case1 = (x+y) * w;

	if ((x+y) % 2 == 0) {
		if (x > y) case2 = x*s;
		else case2 = y*s;
	}
	else {
		if (x > y) case2 = (x-1)*s + w;
		else case2 = (y-1)*s + w;
	}

	if (x > y) case3 = y*s + (x-y)*w;
	else case3 = x*s + (y-x)*w;

	if (case1 < case2 && case1 < case3) printf("%lld\n", case1);
	else if (case2 < case1 && case2 < case3) printf("%lld\n", case2);
	else printf("%lld\n", case3);
}