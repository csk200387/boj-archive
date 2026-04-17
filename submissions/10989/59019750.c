#include <stdio.h>

int main() {
    int arr[10000] = { 0, };
    int n, p, i;
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &p);
        arr[p-1]++;
    }
    for (i = 0; i < 10000; i++) {
        if (arr[i] > 0) {
            for (int t = 0; t < arr[i]; t++) {
                printf("%d\n", i+1);
            }
        }
    }
    return 0;
}