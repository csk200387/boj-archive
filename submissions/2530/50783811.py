a = list(map(int,input().split()))
hou = a[0]
min = a[1]
sec = a[2]
input_sec = int(input())
sec += input_sec
if sec > 59 :
    min += sec//60
    sec = sec%60
    if min > 59 :
        hou += min//60
        min = min%60
        if hou > 23 :
            hou = 0
print(hou,min,sec)