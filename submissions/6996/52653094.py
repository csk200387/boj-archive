for i in range(int(input())) :
    a, b = input().split()
    if set(a)==set(b) and len(a) == len(b) :
        print(f"{a} & {b} are anagrams.")
    else :
        print(f"{a} & {b} are NOT anagrams.")