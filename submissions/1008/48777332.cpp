#include <stdio.h>

int main()
{
    int num1;
    int num2;
    scanf("%d %d", &num1, &num2);

    printf("%lf\n", (double) num1 / (double) num2);

    return 0;
}