#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i, j;
    if (scanf("%d", &n) != 1) exit(0);
    for (i = 1; i <= n; i++) {
        for (j = 1; j < i; j++) {
            printf(" ");
        }
        for (j = n-i; j >= 0; j--) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}