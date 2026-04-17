#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    char a[4];
    char b[4];
    int i;
    scanf("%s %s", a, b);



    if (a[2] == b[2])
    {
        if (a[1] == b[1])
        {
            if (a[0] == b[0])
            {
                for (i = 2; i >= 0; i--)
                {
                    printf("%c", a[i]);
                }
            } 
            else if (a[0] > b[0])
            {
                for (i = 2; i >= 0; i--)
                {
                    printf("%c", a[i]);
                }
            }
            else if (b[0] > a[0])
            {
                for (i = 2; i >= 0; i--)
                {
                    printf("%c", b[i]);
                }
            }
        }
        else if(a[1]>b[1])
        {
            for (i = 2; i >= 0; i--)
            {
                printf("%c", a[i]);
            }
        }
        else if (b[1] > a[1])
        {
            for (i = 2; i >= 0; i--)
            {
                printf("%c", b[i]);
            }
        }
    }
    else if (a[2] > b[2])
    {
        for (i = 2; i >= 0; i--)
        {
            printf("%c", a[i]);
        }
    }
    else if (b[2] > a[2])
        for (i = 2; i >= 0; i--)
        {
            printf("%c", b[i]);
        }
}