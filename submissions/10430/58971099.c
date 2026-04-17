#include <stdio.h>
#include <stdlib.h>
int main() {
    int A, B, C;
    if (scanf("%d %d %d", &A, &B, &C) != 3) {
        exit(0);
    }
    printf("%d\n", (A+B)%C);
    printf("%d\n", ((A%C) + (B%C))%C);
    printf("%d\n", (A*B)%C);
    printf("%d", ((A%C) * (B%C))%C);
}