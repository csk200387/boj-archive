#include <stdio.h>
#include <stdlib.h>
int main() {
    int a, b;
    if (scanf("%d", &a) != 1) {
        exit(0);
    }
    if (scanf("%d", &b) != 1) {
        exit(0);
    }
    printf("%d\n", a*(b%10));
    printf("%d\n", a*((b/10)%10));
    printf("%d\n", a*(b/100));
    printf("%d", a*b);
}