#include <stdio.h>
#include <stdlib.h>

int check(int arr[], int size) {
    for (int i = 1; i < size/2; i++) {
        if (arr[i] != arr[0]) {
            return 0;
        }
    }
    return 1;
}


int main() {
	int size;
	if (scanf("%d", &size) != 1) exit(0);
	int arr[size];
	int diff_a[size-1]; // 등차수열
	int diff_g[size-1]; // 등비수열
	for (int i = 0; i < size; i++) {
		if (scanf("%d", &arr[i]) != 1) exit(0);
	}
	for (int i = 1; i < size; i++) {
		diff_a[i-1] = arr[i] - arr[i-1];
		diff_g[i-1] = arr[i] / arr[i-1];
	}

	if (check(diff_a, size)) {
		printf("%d\n", arr[size-1]+diff_a[1]); //
	} else {
		printf("%d\n", arr[size-1] * diff_g[size-2]);
	}
}