#include <stdio.h>
long long A, B, C;
long long prob(long long n) {
  if (n == 1) {
    return A % C;
  } else if (n % 2 == 0) {
    long long a = prob(n / 2);
    return a * a % C;
  } else {
    long long a = prob(n / 2);
    return a * a * A % C;
  }
}

int main() {
  scanf("%lld %lld %lld", &A, &B, &C);
  printf("%lld\n", prob(B));
  return 0;
}