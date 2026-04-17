#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isPalindrome(char* str) {
    int i = 0, j = strlen(str) - 1;
    while (i < j) {
        if (str[i] != str[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

int main() {
    char input[1001];
    char* arr[101];
    int n, i;
    long long result = 0;
    if (scanf("%d\n", &n) != 1) exit(0);
    if (fgets(input, sizeof(input), stdin) == NULL) exit(0);
    input[strlen(input) - 1] = '\0';
    char* token = strtok(input, " ");
    i = 0;
    while (token != NULL) {
        arr[i++] = token;
        token = strtok(NULL, " ");
    }
    for (i = 0; i < n; i++) {
        if (isPalindrome(arr[i])) {
            result += atoi(arr[i]);
        }
    }
    printf("%lld\n", result);
    return 0;
}