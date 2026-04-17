AB = list(map(int,input().split()))
CD = list(map(int,input().split()))
print(max(AB)+min(CD) if sum(AB) <= sum(CD) else max(CD)+min(AB))