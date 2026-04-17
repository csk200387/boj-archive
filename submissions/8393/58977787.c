#include <stdio.h>
#include <stdlib.h>
int main() {
    int a;
    if (scanf("%d", &a) != 1) exit(0);
    printf("%d", a*(a+1)/2);
    return 0;
}