#include <stdio.h>
#include <stdlib.h>
int main() {
    int a, b, c;
    if (scanf("%d %d", &a, &b) != 2) {
        exit(0);
    }
    c = b - 45;
    if (c < 0) {
        a --;
        if (a < 0) a = 23;
        c += 60;
    }
    printf("%d %d\n", a, c);
}