arr = list(map(str.strip, open(0)))
n,idx = 0, 0
for i in range(3):
    if arr[i].isdigit():
        n = int(arr[i])
        idx = i
        break
res = n+3-idx
if res%3 == 0 and res%5 == 0:
    print("FizzBuzz")
elif res%3 == 0:
    print("Fizz")
elif res%5 == 0:
    print("Buzz")
else:
    print(str(res))