#include <stdio.h>
#include <stdlib.h>

int gcd(int, int);

int main() {
    int a, b;
    if (scanf("%d %d", &a, &b) != 2) exit(0);
    printf("%d\n", (a*b)/gcd(a,b));
    return 0;
}
int gcd(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}