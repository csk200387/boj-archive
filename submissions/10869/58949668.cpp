#include <stdio.h>
#include <stdlib.h>

int main() {
  int a,b;
  if (scanf("%d %d", &a, &b) == 2) {
    printf("%d\n%d\n%d\n%d\n%d", a+b, a-b, a*b, a/b, a%b);
  } else {
    exit(0);
  }
  return 0;
}