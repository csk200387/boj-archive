#include <stdio.h>
#include <stdlib.h>

int main() {
    char arr[10000];
    long long int i = 0;
    if (fscanf(stdin, "%s", arr) != 1) exit(1);

    // check "0" in arr
    int j = 0;
    while (1) {
        if (arr[j] == '0') break;
        if (arr[j] == '\0') {
            printf("-1\n");
            exit(0);
        }
        j++;
    }
    // sorting arr in descending order
    int k = 0;
    while (arr[k] != '\0') {
        int l = k + 1;
        while (arr[l] != '\0') {
            if (arr[k] < arr[l]) {
                char tmp = arr[k];
                arr[k] = arr[l];
                arr[l] = tmp;
            }
            l++;
        }
        k++;
    }

    // sum arr's each element
    int sum = 0;
    int m = 0;
    while (arr[m] != '\0') {
        sum += arr[m] - '0';
        m++;
    }
    if (sum % 3 != 0) {
        printf("-1\n");
        exit(0);
    }
    // print arr
    while (arr[i] != '\0') {
        printf("%c", arr[i]);
        i++;
    }
    printf("\n");
}