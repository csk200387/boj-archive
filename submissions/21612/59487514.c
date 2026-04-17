#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    int i = n*5-400;
    printf("%d\n", i);
    if (n == i) printf("0");
    else if (n > i) printf("1");
    else printf("-1");
    return 0;
}