from math import ceil
b,a = map(int, input().split())
string = ["   "]*(b-1)
for i in range(1, a+1):
    string += [str(i).rjust(3, " ")]
print("Sun Mon Tue Wed Thr Fri Sat")
for i in range(ceil(len(string)/7)):
    i = i*7
    t = string[i:i+7]
    print(*t, sep=" ")