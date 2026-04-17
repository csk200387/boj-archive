# ChatGPT
def min_scalar_product(n, v1, v2):
    v1_sorted = sorted(v1, reverse=True)
    v2_sorted = sorted(v2)
    scalar_product = sum(v1_sorted[i] * v2_sorted[i] for i in range(n))
    return scalar_product

T = int(input())

for i in range(1, T+1):
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    min_product = min_scalar_product(n, v1, v2)
    print(f"Case #{i}: {min_product}")