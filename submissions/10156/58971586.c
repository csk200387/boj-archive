#include <stdio.h>
#include <stdlib.h>
int main() {
    int a, b, c;
    if (scanf("%d %d %d", &a, &b, &c) != 3) {
        exit(0);
    }
    printf("%d", (a*b)-c > 0 ? (a*b)-c : 0);
}