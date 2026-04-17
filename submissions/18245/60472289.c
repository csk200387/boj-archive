#include <stdio.h>
#include <string.h>

int main() {
    char s[10001];
    int i = 2;
    while (1) {
        fgets(s, sizeof(s), stdin);
        s[strcspn(s, "\n")] = '\0';
        if (!strcmp(s, "Was it a cat I saw?")) break;
        for (int j = 0; j < strlen(s); j += i) {
            printf("%c", s[j]);
        }
        printf("\n");
        i++;
    }
    return 0;
} 
