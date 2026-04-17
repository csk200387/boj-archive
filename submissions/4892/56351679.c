#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n0, n1, n2, n3, n4;
    char res[4] = "even";
    for (int stack = 1; 1; stack++) {
        if (scanf("%d", &n0) == 0) {
           exit(0);
        }
        if (n0 == 0) {
            break;
        } else {
            n1 = n0*3;
            if ((n1 & 1) == 0) {
					n2 = n1/2;
				} else {
					n2 = (n1+1)/2;
                    strcpy(res, "odd");
				}
				n3 = n2*3;
				n4 = n3/9;
				printf("%d. %s %d\n", stack, res, n4);
        }
    }
}