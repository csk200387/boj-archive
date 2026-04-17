#include <stdio.h>

void isPalindrome(char *str);

int main() {
	while (1) {
		char arr[100000];
		if (scanf("%s", arr) != 1) return 0;
		if (arr[0] == '0') return 0;
		isPalindrome(arr);
	}
}

void isPalindrome(char *str) {
	int i = 0, j = 0;
	while (str[i] != '\0') i++;
	i--;
	while (j < i) {
		if (str[j] != str[i]) {
			printf("no\n");
			return;
		}
		j++;
		i--;
	}
	printf("yes\n");
}