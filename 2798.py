card_n, sum_limit = list(map(int, input().split()))
cards = list(map(int, input().split()))
assert len(cards) == card_n

result = -1

for i in range(card_n):
    for j in range(i+1, card_n):
        for k in range(j+1, card_n):
            tmp = cards[i] + cards[j] + cards[k]
            if result < tmp <= sum_limit:
                result = tmp

print(result)