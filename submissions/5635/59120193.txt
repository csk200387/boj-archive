// Github Copilot
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();

        String mx = "";
        String mn = "";
        int mx_date = 0;
        int mn_date = 9999;
        int mx_month = 0;
        int mn_month = 9999;
        int mx_year = 0;
        int mn_year = 9999;

        for (int i = 0; i < n; i++) {
            String name = sc.next();
            int date = sc.nextInt();
            int month = sc.nextInt();
            int year = sc.nextInt();

            if (year > mx_year) {
                mx_year = year;
                mx_month = month;
                mx_date = date;
                mx = name;
            } else if (year == mx_year) {
                if (month > mx_month) {
                    mx_year = year;
                    mx_month = month;
                    mx_date = date;
                    mx = name;
                } else if (month == mx_month) {
                    if (date > mx_date) {
                        mx_year = year;
                        mx_month = month;
                        mx_date = date;
                        mx = name;
                    }
                }
            }

            if (year < mn_year) {
                mn_year = year;
                mn_month = month;
                mn_date = date;
                mn = name;
            } else if (year == mn_year) {
                if (month < mn_month) {
                    mn_year = year;
                    mn_month = month;
                    mn_date = date;
                    mn = name;
                } else if (month == mn_month) {
                    if (date < mn_date) {
                        mn_year = year;
                        mn_month = month;
                        mn_date = date;
                        mn = name;
                    }
                }
            }
        }

        System.out.println(mx);
        System.out.println(mn);
    }
}