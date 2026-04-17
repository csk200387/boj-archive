#include <stdio.h>
#include <math.h>

int main() {
    float a, b, c, d, e;
    scanf("%f", &a);
    scanf("%f", &b);
    scanf("%f", &c);
    scanf("%f", &d);
    scanf("%f", &e);
    int res = pow(a,2.0) + pow(b,2.0) + pow(c,2.0) + pow(d,2.0) + pow(e,2.0);
    printf("%d", res%10);
    return 0;
}