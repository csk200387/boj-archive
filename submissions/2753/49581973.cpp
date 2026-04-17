#include <stdio.h>
//윤년은 1 평년은 0
int main()
{
  int year;
  scanf("%d",&year);
  if(year%4 == 0){
    if(year%400 != 0 && year%100 == 0)
      printf("0");
    else
      printf("1");
  }
  else
    printf("0");
  return 0;
}