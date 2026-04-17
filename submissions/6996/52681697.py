for i in range(int(input())) :
    a,b=input().split()
    c=""
    if sorted(a)!=sorted(b) :
        c="NOT "
    print(f"{a} & {b} are {c}anagrams.")