#include <stdio.h>

int main() {
    int arr[3][3];

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            scanf("%d", &arr[i][j]);
        }
    }
    if (arr[0][0] == 9) {
        if (arr [0][1] != 9) arr [0][1] += 1;
        if (arr [1][0] != 9) arr [1][0] += 1;
        if (arr [1][1] != 9) arr [1][1] += 1;
    }
     if (arr[0][1] == 9) {
        if (arr [0][0] != 9) arr [0][0] += 1;
        if (arr [0][2] != 9) arr [0][2] += 1;
        if (arr [1][0] != 9) arr [1][0] += 1;
        if (arr [1][1] != 9) arr [1][1] += 1;
        if (arr [1][2] != 9) arr [1][2] += 1;
    }
     if (arr[0][2] == 9) {
        if (arr [0][1] != 9) arr [0][1] += 1;
        if (arr [1][1] != 9) arr [1][1] += 1;
        if (arr [1][2] != 9) arr [1][2] += 1;
        
    }
     if (arr[1][0] == 9) {
        if (arr [0][0] != 9) arr [0][0] += 1;
        if (arr [0][1] != 9) arr [0][1] += 1;
        if (arr [1][1] != 9) arr [1][1] += 1;
        if (arr [2][0] != 9) arr [2][0] += 1;
        if (arr [2][1] != 9) arr [2][1] += 1;
    }
     if (arr[1][1] == 9) {
        if (arr [0][0] != 9) arr [0][0] += 1;
        if (arr [0][1] != 9) arr [0][1] += 1;
        if (arr [0][2] != 9) arr [0][2] += 1;
        if (arr [1][0] != 9) arr [1][0] += 1;
        if (arr [1][2] != 9) arr [1][2] += 1;
        if (arr [2][0] != 9) arr [2][0] += 1;
        if (arr [2][1] != 9) arr [2][1] += 1;
        if (arr [2][2] != 9) arr [2][2] += 1;
    }
    if (arr[1][2] == 9) {
        if (arr [0][1] != 9) arr [0][1] += 1;
        if (arr [0][2] != 9) arr [0][2] += 1;
        if (arr [1][1] != 9) arr [1][1] += 1;
        if (arr [2][1] != 9) arr [2][1] += 1;
        if (arr [2][2] != 9) arr [2][2] += 1;
    }
    if (arr[2][0] == 9) {
        if (arr [1][0] != 9) arr [1][0] += 1;
        if (arr [1][1] != 9) arr [1][1] += 1;
        if (arr [2][1] != 9) arr [2][1] += 1;
    }
    if (arr[2][1] == 9) {
        if (arr [1][0] != 9) arr [1][0] += 1;
        if (arr [1][1] != 9) arr [1][1] += 1;
        if (arr [1][2] != 9) arr [1][2] += 1;
        if (arr [2][0] != 9) arr [2][0] += 1;
        if (arr [2][2] != 9) arr [2][2] += 1;
    }
    if (arr[2][2] == 9) {
        if (arr [1][1] != 9) arr [1][1] += 1;
        if (arr [1][2] != 9) arr [1][2] += 1;
        if (arr [2][1] != 9) arr [2][1] += 1;
    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

}