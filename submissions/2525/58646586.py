h, m = map(int, input().split())
m = m + int(input())
if m >= 60:
	h = h + m / 60;
	m = m % 60;
if h >= 24 :
    h = h % 24
print(f"{h:.0f} {m:.0f}")