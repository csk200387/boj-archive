#include <stdio.h>

int main() {
    
    unsigned long long N = 0;
    int cnt;
    scanf("%d ", &cnt);
    while (cnt != EOF) {
        int tmp;
        scanf("%d ", &tmp);
        N += tmp;
    }
    printf("%lld\n", N);

    return 0;
}