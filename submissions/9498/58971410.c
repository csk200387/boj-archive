#include <stdio.h>
#include <stdlib.h>
int main() {
    int n;
    if (scanf("%d", &n) != 1) {
        exit(0);
    }
    if (90 <= n) printf("A");
    else if (80 <= n) printf("B");
    else if (70 <= n) printf("C");
    else if (60 <= n) printf("D");
    else printf("F");
}