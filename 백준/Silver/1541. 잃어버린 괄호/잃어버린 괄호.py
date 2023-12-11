form = input().split('-')
result = 0
for i in form[0].split('+'):
    result += int(i)
for i in range(1,len(form)):
    for j in form[i].split('+'):
        result -= int(j)
print(result)