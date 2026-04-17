#include <stdio.h>
#include <stdlib.h>

int gcd(long int, long int);

int main() {
    long int a, b;
    if (scanf("%ld %ld", &a, &b) != 2) exit(0);
    printf("%ld\n", (a*b)/gcd(a,b));
    return 0;
}
int gcd(long int a, long int b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}