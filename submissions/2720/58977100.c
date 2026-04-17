#include <stdio.h>
#include <stdlib.h>
int main() {
    int r, c, q, d, n, p;
    if (scanf("%d", &r) != 1) {
        exit(0);
    }
    for (int i = 0; i < r; i++) {
        if (scanf("%d", &c) != 1) {
           exit(0);
        }
        q = c / 25;
        d = (c % 25) / 10;
        n = ((c % 25) % 10) / 5;
        p = c % 5;
        printf("%d %d %d %d\n", q, d, n, p);
    }
}