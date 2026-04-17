from collections import deque
data = list(input())

grades = {
    'A+': 0,
    'A': 0,
    'B+': 0,
    'B': 0,
    'C+': 0,
    'C': 0,
    'D+': 0,
    'D': 0,
    'F': 0
}

score = {
    'A+': 4.5,
    'A': 4.0,
    'B+': 3.5,
    'B': 3.0,
    'C+': 2.5,
    'C': 2.0,
    'D+': 1.5,
    'D': 1.0,
    'F': 0
}

stack = deque()

while data:
    stack.appendleft(data.pop())

    if stack[-1] == '+' and len(stack) > 1:
        if stack[-2] == 'A':
            grades['A+'] += 1
        elif stack[-2] == 'B':
            grades['B+'] += 1
        elif stack[-2] == 'C':
            grades['C+'] += 1
        elif stack[-2] == 'D':
            grades['D+'] += 1
        stack.pop()
        stack.pop()
    elif stack[-1] == '+' and len(stack) == 1:
        continue
    else:
        grades[stack.pop()] += 1

print(stack)
print(data)
print(grades)

avg = 0
for key, value in grades.items():
    avg += score[key] * value

print(f'{avg / sum(grades.values()):.5f}'.rstrip('0'))