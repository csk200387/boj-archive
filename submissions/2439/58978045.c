#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, i, j;
    if (scanf("%d", &a) != 1) exit(0);
    for (i = 0; i < a; i++) {
        for (j = 1; j < a-i; j++) printf(" ");
        for (j = 0; j <= i; j++) printf("*");
        printf("\n");
    }
    return 0;
}