#include <stdio.h>
#include <stdlib.h>

int main() {
    char c;
    scanf("%c", &c);
    printf("%d\n", 84+abs(c-73));
    return 0;
}