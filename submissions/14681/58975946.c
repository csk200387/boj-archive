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
    printf("%d", a>0 ? (b>0 ? 1 : 4) : (a>0 ? 2 : 3));
}