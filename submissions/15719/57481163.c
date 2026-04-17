#include<stdio.h>
int main(){
	int size, t, sum = 0;
	if (scanf("%d", &size) != 1) {
		return 0;
	} else {
		for (int i = 0; i < size; i++) {
			if (scanf("%d", &t) != 1) {
				return 0;
			} else {
				sum += t;
			}
		}
	}
	printf("%d\n", size+sum-(int)(size*(size+1)/2));
}