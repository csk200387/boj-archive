import math
import sys
input = lambda:sys.stdin.readline().rstrip()

grades = {
    'A+': 450,
    'A0': 400,
    'B+': 350,
    'B0': 300,
    'C+': 250,
    'C0': 200,
    'D+': 150,
    'D0': 100,
    'F': 0
}
score = 0
gd = 0
n, avg = input().split()
avg = int(avg.replace(".", ""))

for i in range(int(n)-1):
    c, g = input().split()
    gd += int(c)*100
    score += int(c)*100 * grades[g]

last = int(input())*100

for key, value in reversed(grades.items()):
    if int(((score + value*last) / (gd+last))) > avg:
        print(key)
        exit()

print("impossible")