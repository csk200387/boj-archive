#include <stdio.h>

int main() {
    int a, b, c, d, e;
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
    int res = a*a + b*b + c*c+ d*d + e*e;
    printf("%d", res%10);
    return 0;
}