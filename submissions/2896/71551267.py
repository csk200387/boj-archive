ingred = list(map(int, input().split()))
ratio = list(map(int, input().split()))
m = min(ingred[i]/ratio[i] for i in range(3))
for i in range(3):
    print(ingred[i]-ratio[i]*m, end=" ")