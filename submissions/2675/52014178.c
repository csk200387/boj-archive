#include <stdio.h>
#include <ctype.h>

int main() {
    int try;
    scanf("%d", &try);
    for (int i = 0; i < try; i++) {
        int r;
        char str;
        scanf("%d ", &r);
        while (1) {
            scanf("%c", &str);
            if (isspace(str) != 0) {
                break;
            } else {
                for (int l = 0; l < r; l++) {
                    printf("%c",str);
                }
            }
        }
    }
}