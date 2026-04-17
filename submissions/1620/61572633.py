import sys
input = lambda:sys.stdin.readline().rstrip()

N, M = map(int, input().split())

pokemon = {i:input() for i in range(1, N+1)}
reverse_pokemon = {v:k for k, v in pokemon.items()}

for _ in range(M):
    q = input()
    if q.isdigit():
        print(pokemon[int(q)])
    else:
        print(reverse_pokemon[q])