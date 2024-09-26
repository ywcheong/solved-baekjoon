n = int(input())

for _ in range(n):
    n, text = input().split()
    n = int(n)

    result = ""
    for s in text:
        result += s * n
    print(result)