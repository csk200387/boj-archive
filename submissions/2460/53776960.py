arr = []
person = 0
for i in range(10) :
    IN, OUT = map(int, input().split())
    person += OUT-IN
    arr.append(person)
print(max(arr))