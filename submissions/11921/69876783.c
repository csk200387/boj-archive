#include <stdio.h>

int main() {
    
    unsigned long long N = 0;
    int cnt;
    scanf("%d ", &cnt);
    cnt = 0;
    while (cnt != EOF) {
        scanf("%d ", &cnt);
        N += cnt;
    }
    printf("%lld\n", N);

    return 0;
}
