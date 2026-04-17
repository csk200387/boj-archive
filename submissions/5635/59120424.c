// 참 쉽죠? -밥 로스-
#include <stdio.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);

    char mx[101], mn[101];
    int mx_date = 0, mn_date = 9999;
    int mx_month = 0, mn_month = 9999;
    int mx_year = 0, mn_year = 9999;

    for (int i = 0; i < n; i++) {
        char name[101];
        int date, month, year;
        scanf("%s %d %d %d", name, &date, &month, &year);

        if (year > mx_year) {
            mx_year = year;
            mx_month = month;
            mx_date = date;
            strcpy(mx, name);
        } else if (year == mx_year) {
            if (month > mx_month) {
                mx_year = year;
                mx_month = month;
                mx_date = date;
                strcpy(mx, name);
            } else if (month == mx_month) {
                if (date > mx_date) {
                    mx_year = year;
                    mx_month = month;
                    mx_date = date;
                    strcpy(mx, name);
                }
            }
        }

        if (year < mn_year) {
            mn_year = year;
            mn_month = month;
            mn_date = date;
            strcpy(mn, name);
        } else if (year == mn_year) {
            if (month < mn_month) {
                mn_year = year;
                mn_month = month;
                mn_date = date;
                strcpy(mn, name);
            } else if (month == mn_month) {
                if (date < mn_date) {
                    mn_year = year;
                    mn_month = month;
                    mn_date = date;
                    strcpy(mn, name);
                }
            }
        }
    }

    printf("%s\n%s\n", mx, mn);
    return 0;
}