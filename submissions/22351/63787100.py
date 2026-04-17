def concatenate_range_string(N, M):
    return ''.join(str(i) for i in range(N, M + 1))

def find_concatenated_numbers(s):
    s_int = int(s)
    min_num = 1
    max_num = len(s) // 2 + 1  # 최대 길이의 절반까지만 검사
    for i in range(1, max_num):
        N = int(s[:i])
        M = N
        while len(concatenate_range_string(N, M)) < len(s):
            M += 1
        if s_int == int(concatenate_range_string(N, M)):
            return N, M
    return s_int, s_int

s = input()
result = find_concatenated_numbers(s)
print(result[0], result[1])