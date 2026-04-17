#include <stdio.h>
#include <stdlib.h>

int main() {
    long long int K, N;
    if (scanf("%lld %lld", &K, &N) == 1) {
        printf("-1\n");
        exit(0);
    }
    if (N == 1) {
        printf("-1\n");
        return 0;
    }
    long long int res = N*K / (N-1);
    if ((N*K) % (N-1) != 0) res++;
    printf("%lld\n", res);
    return 0;
}