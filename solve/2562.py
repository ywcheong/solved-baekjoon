ans, index = 0, 0

for i in range(1, 10):
    read = int(input())
    if read > ans:
        ans, index = read, i

print(ans)
print(index)