size = input()

list_ = list(map(int, input().split()))

set_ = set(list_)

sorted_set = list(set_)

sorted_set.sort()

for num in sorted_set:
    print(num, end=" ")