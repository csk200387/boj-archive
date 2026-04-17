import math
def pizza_per_dollar(A1, P1, R1, P2):
    pizza_area = math.pi * R1 ** 2
    slice_pizza_per_dollar = A1 / P1
    whole_pizza_per_dollar = pizza_area / P2
    return 'Slice of pizza' if slice_pizza_per_dollar > whole_pizza_per_dollar else 'Whole pizza'

if __name__ == '__main__':
    A1, P1 = map(int, input().split())
    R1, P2 = map(int, input().split())
    print(pizza_per_dollar(A1, P1, R1, P2))