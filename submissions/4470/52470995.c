#include <stdio.h>
int main() {
	int a, i;
	scanf("%d ", &a);
	for (i = 0; i < a; i++) {
		char arr[51];
		fgets(arr, sizeof(arr), stdin);
		printf("%d. %s", (i+1), arr);
	}	
}