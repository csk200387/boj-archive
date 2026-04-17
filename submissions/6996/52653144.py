from collections import Counter
for i in range(int(input())) :
    a, b = input().split()
    if Counter(a) == Counter(b) :
        print(f"{a} & {b} are anagrams.")
    else :
        print(f"{a} & {b} are NOT anagrams.")