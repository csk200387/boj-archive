s = input().upper()
dic = {}
for i in s :
    try :
        dic[i] += 1
    except :
        dic[i] = 1
dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
a = list(dic.keys())
try :
    if dic[a[0]] == dic[a[1]] :
        print("?")
    else :
        print(a[0])
except :
    print(a[0])