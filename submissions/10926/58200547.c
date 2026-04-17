#include <stdio.h>
#include <string.h>

int main() {
  char c[54];
  char t[4] = "??!";
  scanf("%s", c);
  strcat(c, t);
  printf("%s\n", c);
  return 0;
}