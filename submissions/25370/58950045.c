#include <stdio.h>
#include <stdlib.h>

int main() {
  int arr[8] = { 1, 9, 36, 100, 225, 441, 784, 1296 };
  int a;
  if (scanf("%d", &a) == 1) {
    printf("%d\n", arr[a]);
  } else {
    exit(0);
  }
  return 0;
}