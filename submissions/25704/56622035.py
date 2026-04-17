c = int(input())
p = int(input())
arr = [max(p-500, 0), int(p*0.9), max(p-2000, 0), int(p*0.75)][:c//5]
print(p if not arr else min(arr))