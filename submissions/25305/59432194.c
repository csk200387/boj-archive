#include <stdio.h>

int n_th_smallest(int a[], int size, int n) {
    for (int i = 0; i < n; i++) {
        int min_index = i;
        for (int j = i + 1; j < size; j++) {
            if (a[j] < a[min_index]) {
                min_index = j;
            }
        }
        int temp = a[i];
        a[i] = a[min_index];
        a[min_index] = temp;
    }
    return a[n-1];
}

int main() {
    int size, c;
    if (scanf("%d %d", &size, &c) != 2) return 0;
    int a[size];
    for (int i = 0; i < size; i++) {
        if (scanf("%d", &a[i]) != 1) return 0;
    }
	printf("%d", n_th_smallest(a, size, size-c+1));
}