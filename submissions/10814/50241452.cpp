#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int member, temp1;
    int age[1000001];
    char temp2[101];
    char name[1000001][101];
    scanf("%d", &member);
    for (int i = 1; i < member + 1; i++) {
        scanf("%d %s", &age[i], &name[i - 1][101]);
    }
    for (int i = 1; i <= member; i++) {
        for (int j = 1; j <= member - 1; j++) {
            if (age[j] > age[j + 1]) {
                temp1 = age[j];
                age[j] = age[j + 1];
                age[j + 1] = temp1;
                strcpy(temp2, name[j]);
                strcpy(name[j], name[j + 1]);
                strcpy(name[j + 1], temp2);
                temp1 = 0;
            }
        }
    }
    for (int i = 1; i <= member; i++) {
        printf("%d %s\n", age[i], name[i]);
    }
    return 0;
}