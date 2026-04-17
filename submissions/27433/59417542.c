#include <stdio.h>
#include <stdlib.h>

long int fac(long long int n);

int main() {
    int n;
    if (scanf("%d", &n) != 1) exit(0);
    long long int result = fac(n);
    printf("%lld", result);
}

long int fac(long long int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * fac(n-1);
}