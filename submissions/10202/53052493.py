for _ in range(int(input())) :
    inp = "".join(input().split()[1::]).replace(" ","").split("O")
    print(f"The longest contiguous subsequence of X's is of length {len(max(inp))}")