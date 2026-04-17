n = int(input())

mx = ""
mn = ""
mx_date = 0
mn_date = 99999
mx_month = 0
mn_month = 99999
mx_year = 0
mn_year = 99999

for i in range(n) :
    name, date, month, year = input().split()
    date = int(date)
    month = int(month)
    year = int(year)
    if year > mx_year :
        mx_year = year
        mx_month = month
        mx_date = date
        mx = name
    elif year == mx_year :
        if month > mx_month :
            mx_year = year
            mx_month = month
            mx_date = date
            mx = name
        elif month == mx_month :
            if date > mx_date :
                mx_year = year
                mx_month = month
                mx_date = date
                mx = name
    if year < mn_year :
        mn_year = year
        mn_month = month
        mn_date = date
        mn = name
    elif year == mn_year :
        if month < mn_month :
            mn_year = year
            mn_month = month
            mn_date = date
            mn = name
        elif month == mn_month :
            if date < mn_date :
                mn_year = year
                mn_month = month
                mn_date = date
                mn = name
                
print(mx)
print(mn)