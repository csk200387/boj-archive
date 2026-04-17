#include <stdio.h>

int main() {
    int x1, y1;
    if (scanf("%d %d", &x1, &y1) != 2) return 0;
    int arr[x1][y1];
    for (int i = 0; i < x1; i++) {
        for (int j = 0; j < y1; j++) {
            if (scanf("%d", &arr[i][j]) != 1) return 0;
        }
    }

    int x2, y2;
    if (scanf("%d %d", &x2, &y2) != 2) return 0;
    int arr2[x2][y2];
    for (int i = 0; i < x2; i++) {
        for (int j = 0; j < y2; j++) {
            if (scanf("%d", &arr2[i][j]) != 1) return 0;
        }
    }

    int result[x1][y2];

    for (int i = 0; i < x1; i++) {
        for (int j = 0; j < y2; j++) {
            result[i][j] = 0;
            for (int k = 0; k < y1; k++) {
                result[i][j] += arr[i][k] * arr2[k][j];
            }
        }
    }

    for (int i = 0; i < x1; i++) {
        for (int j = 0; j < y2; j++) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }
    return 0;
}