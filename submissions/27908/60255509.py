from math import ceil
a,b = map(int, input().split())
string = "..."*(b-1)
for i in range(1, a+1):
    string += str(i).rjust(3, ".")
print("+"+"-"*21+"+")
for i in range(ceil(len(string)/21)):
    i = i*21
    t = string[i:i+21]
    print("|"+t+"."*(21-len(t))+"|")
print("+"+"-"*21+"+")