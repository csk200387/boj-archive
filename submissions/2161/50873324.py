a = int(input())
card = list(range(1,a+1))
while len(card) != 1 :
    a = card.pop(0)
    print(a, end=" ")
    card.append(card.pop(0))
print(card[0])