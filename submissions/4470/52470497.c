#include <stdio.h>
int main() {
	int a, i;
	scanf("%d ", &a);
	for (i = 0; i < a; i++) {
		char arr[51];
		scanf(" %[^\n]s", arr);
		printf("%d. %s", (i+1), arr);
	}	
}