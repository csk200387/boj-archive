#include <stdio.h>

int gcd(int a, int b) {
    int tmp, n;

    if(a<b){
        tmp = a;
        a = b;
        b = tmp;
    }

    while(b!=0) {
        n = a%b;
        a = b;
        b = n;
    }
    return a;
}

void main() {
    int n, a, b;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &a, &b);

        printf("%d\n", (a * b) / gcd(a,b));
    }
}