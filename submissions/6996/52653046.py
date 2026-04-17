for i in range(int(input())) :
    a, b = input().split()
    print(f"{a} & {b} are anagrams." if set(a)==set(b) else f"{a} & {b} are NOT anagrams.")