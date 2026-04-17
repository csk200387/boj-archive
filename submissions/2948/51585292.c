#include <stdio.h>
int main() {
	int mon, date, a;
	int mnum[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	char* day[7] = {"Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"};
	scanf("%d %d", &date, &mon);
	if(mon ==1) a = date%7;
	else {
		int b =0;
		for(int i =0; i < mon; i ++){
			b += mnum[i -1];
		}
		a = (b +date)%7;
	}
	printf("%s", day[a]);
	return 0;
}