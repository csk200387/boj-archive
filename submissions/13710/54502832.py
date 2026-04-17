def XOR_sum_of_subsequence(A):
    n = len(A)
    result = 0
    for i in range(n):
        for j in range(i,n):
            sub_seq = A[i:j+1]
            xor_sum = sub_seq[0]
            for k in range(1,len(sub_seq)):
                xor_sum ^= sub_seq[k]
            result += xor_sum
    return result
input()
print(XOR_sum_of_subsequence(list(map(int, input().split()))))