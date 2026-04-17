import sys
import functools

def custom_sort(strings):
    def compare(x, y):
        i = 0
        j = 0
        while i < len(x) and j < len(y):
            if x[i] == '-' and y[j] != '-':
                return 1
            elif x[i] != '-' and y[j] == '-':
                return -1
            elif x[i].lower() != y[j].lower():
                return ord(x[i]) - ord(y[j]) if x[i].lower() < y[j].lower() else ord(x[i]) - ord(y[j])
            i += 1
            j += 1
        return len(x) - len(y) if len(x) != len(y) else 0

    return sorted(strings, key=functools.cmp_to_key(compare))


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        strings = [input().strip() for _ in range(n)]
        result = custom_sort(strings)
        for s in result:
            print(s)