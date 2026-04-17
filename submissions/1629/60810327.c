#include <stdio.h>

int A, B, C;
long long prob(int n) {
    if (n == 1) return A%C;
    if (n % 2 == 0) {
        long long a = prob(n/2);
        return a * a % C;
    } else {
        long long a = prob(n/2);
        return a * a * A % C;
    }
}
int main() {
    if (scanf("%d %d %d", &A, &B, &C) != 3) return 0;
    long long result = prob(B);
    printf("%lld\n", result);
    return 0;
}