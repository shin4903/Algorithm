N = int(input())
result = 0
words = []
temp = []
for _ in range(N):
    words.append(input())

for word in words:
    temp.clear()
    for alpha in word:
        if alpha in temp:
            if temp[-1] == alpha:
                continue
            else:
                break
        elif alpha not in temp:
            temp.append(alpha)
    else:
        result += 1
print(result)