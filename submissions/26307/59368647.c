#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b;
    if (scanf("%d %d", &a, &b) != 2) exit(0);
    printf("%d\n", b+60*(a-9));
    return 0;
}