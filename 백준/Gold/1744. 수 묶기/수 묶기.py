N = int(input())
plus = []
minus = []
result = 0
for _ in range(N):
    i = int(input())
    if i > 1:
        plus.append(i)
    elif i == 1:
        result += 1
    else:
        minus.append(i)
plus.sort(reverse=True)

minus.sort()
while plus:
    if len(plus) >= 2:
        result += plus.pop(0) * plus.pop(0)
    elif len(plus) == 1:
        result += plus.pop(0)
while minus:
    if len(minus) >= 2:
        result += minus.pop(0) * minus.pop(0)
    elif len(minus) == 1:
        result += minus.pop(0)

print(result)