import math

def check(cm, kg) :
    bmi = kg / (cm / 100) ** 2
    if cm < 140.1:
        return 6
    elif 140.1 <= cm < 146:
        return 5
    elif 146 <= cm < 159:
        return 4
    elif 159 <= cm < 161:
        if 16 <= bmi < 35:
            return 3
        else:
            return 4
    elif 161 <= cm < 204:
        if 20 <= bmi < 25:
            return 1
        elif (18.5 <= bmi < 20) or (25 <= bmi < 30):
            return 2
        elif (16 <= bmi < 18.5) or (30 <= bmi < 35):
            return 3
        else:
            return 4
    else:
        return 4

t = int(input())
for i in range(t):
    cm, kg = map(float, input().split())
    print(check(cm, kg))
