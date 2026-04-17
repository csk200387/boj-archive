import calendar
calendar.setfirstweekday(calendar.SUNDAY)
year = int(input())
input()
cnt = 0
for mon in range(1, 13):
    tmp = [0] * 7
    for arr in calendar.monthcalendar(year, mon):
        for i in range(7):
            if arr[i] != 0:
                tmp[i] += 1
    for i in tmp:
        if i == 5:
            cnt += 1
print(cnt)