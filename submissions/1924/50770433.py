day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
inp = list(map(int,input().split()))
mon = inp[0]
date = inp[1]
for i in range(1,mon):
    if i == 2 :
        date += 28
    if i in [1,3,5,7,8,10,12] :
        date += 31
    if i in [4,6,9,11] :
        date += 30
print(day[date%7])