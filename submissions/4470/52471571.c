#include <stdio.h>
int main() {
	int a, i;
	scanf("%d ", &a);
	char arr[a][50];
	for (i = 0; i < a; i++) {
		gets(arr[i]);
	}
	for (i = 0; i < a; i++) {
		printf("%d. %s\n", (i+1), arr[i]);
	}	
}