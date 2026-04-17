#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	int a, b;
	int arr[1000];
	char str[1000], * s;
	int cnt = 0;
	scanf("%d %d\n", &a, &b);

	fgets(str);

	for (s = strtok(str, " "); s; s = strtok(NULL, " "), cnt++) // strtok 에 구분자 지정
		if (sscanf(s, "%d", &arr[cnt]) < 1)
			break;

	for (int i = 0; i < a; i++) {
		for (int l = 0; l < a; l++) {
			if (arr[i] < arr[i + l]) {
				int temp = arr[i];
				arr[i] = arr[i + l];
				arr[i + l] = temp;
			}
		}
	}
	printf("%d", arr[b - 1]);
	return 0;
}