#include <stdio.h>
#include <stdlib.h>

int main() {
    int r;
    if (scanf("%d ", &r) != 1) {
        exit(0);
    }
    for (int i = 0; i < r; i++) {
        int a,b;
        if (scanf("%d %d ", &a, &b) != 2) {
            exit(0);
        }
        printf("%d\n", a+b);
    }
}