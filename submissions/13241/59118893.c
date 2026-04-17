#include <stdio.h>
#include <stdlib.h>

int gcd(long long int, long long int);

int main() {
    long long int a, b;
    if (scanf("%lld %lld", &a, &b) != 2) exit(0);
    printf("%lld\n", (a*b)/gcd(a,b));
    return 0;
}
int gcd(long long int a, long long int b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}