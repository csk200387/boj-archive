c = int(input())
p = int(input())
arr = [max(p-500, 0), int(p*0.9), max(p-2000, 0), int(p*0.75)]
try : print(min(arr[:c//5]))
except ValueError : print(0)