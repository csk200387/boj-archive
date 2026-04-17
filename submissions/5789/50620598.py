num = int(input())
for i in range(num) :
    a = input()
    l = int(len(a)/2)
    print("Do-it" if a[l-1] == a[l] else "Do-it-Not")