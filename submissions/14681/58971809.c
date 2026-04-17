#include <stdio.h>
#include <stdlib.h>
int main() {
    int a, b;
    if (scanf("%d %d", &a, &b) != 2) {
        exit(0);
    }
    printf("%s",a>0 ? (b>0 ? "1" : "4") : (a>0?"2":"3"));
}