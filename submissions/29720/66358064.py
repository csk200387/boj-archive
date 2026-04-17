a,b,c = map(int, input().split())
t = a-b*c
print(max(0,t), max(0,t+b-1))