size = int(input())
left_cards = list(map(int, input().split()))
right_cards = list(map(int, input().split()))

memo = [[None] * (size+1) for _ in range(size+1)]
for lcard in range(size, -1, -1):
    for rcard in range(size, -1, -1):
        result = None

        if lcard == size or rcard == size:
            result = 0
        else:
            result = max(
                memo[lcard + 1][rcard + 1],
                memo[lcard + 1][rcard],
                (memo[lcard][rcard + 1] + right_cards[rcard]) if right_cards[rcard] < left_cards[lcard] else 0
            )

        memo[lcard][rcard] = result

print(memo[0][0])