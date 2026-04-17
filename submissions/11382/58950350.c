#include <stdio.h>
#include <stdlib.h>

int main() {
  long arr[3];
  if (scanf("%ld %ld %ld", &arr[0], &arr[1], &arr[2]) == 3) {
    printf("%ld\n", arr[0]+arr[1]+arr[2]);
  } else {
    exit(0);
  }
  return 0;
}