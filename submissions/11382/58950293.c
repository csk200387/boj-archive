#include <stdio.h>
#include <stdlib.h>

int main() {
  int arr[3];
  if (scanf("%d %d %d", &arr[0], &arr[1], &arr[2]) == 3) {
    printf("%d\n", arr[0]+arr[1]+arr[2]);
  } else {
    exit(0);
  }
  return 0;
}