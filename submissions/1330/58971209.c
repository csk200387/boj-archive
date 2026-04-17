#include <stdio.h>
#include <stdlib.h>
int main() {
    int A, B;
    if (scanf("%d %d", &A, &B) != 2) {
        exit(0);
    }
    if (A < B) printf("<");
    else if (A == B) printf("==");
    else printf(">");
}