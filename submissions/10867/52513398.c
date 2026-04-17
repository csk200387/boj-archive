#include <stdio.h>

int main() {
	int n, tmp;
	int arr[1000] = { 0, };
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &tmp);
		arr[tmp-1] = 1;
	}
	for (int i = 0; i < 1000; i++) {
		if (arr[i] == 1) printf("%d ", i+1);
	}
}