#include <stdio.h>
#include <stdlib.h>

int main() {
    long long a, b;
    if (scanf("%lld %lld", &a, &b) == 2) {
        while (b > 0) {
            long long t = b;
            b = a % b;
            a = t;
        }
        for (int i = 0; i < a; i++) {
            printf("1");
        }
    } else {
        exit(0);
    }
}