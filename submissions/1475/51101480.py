import math
inp = list(input().replace("9","6"))
dic = {}

for i in inp :
    try :
        dic[i] += 1
    except :
        dic[i] = 1
try : 
    dic["6"] = math.ceil(dic["6"]/2)
except :
    pass
print(max(dic.values()))