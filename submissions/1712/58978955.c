#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b, c;
    if (scanf("%d %d %d", &a, &b, &c) != 3) exit(0);
    if (c-b <= 0) printf("-1");
    else printf("%d", a/(c-b)+1);
    return 0;
} 