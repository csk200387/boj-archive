#include <stdio.h>
int main(void) {
    char a[4];
    char b[4];
    int i, t;
    scanf("%s %s", a, b);
    for (t = 2; t >= 0; t--) {
        if (a[t] > b[t]) {
            for (i = 2; i >= 0; i--)
                printf("%c", a[i]);
            break;
        }
        else if (b[t] > a[t])
        {
            for (i = 2; i >= 0; i--)
                printf("%c", b[i]);
            break;
        }
    }
    return 0;
}