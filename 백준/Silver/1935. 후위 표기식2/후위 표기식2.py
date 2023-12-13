N = int(input())
alpha = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11,'M':12, 'N':13,
         'O':14, 'P':15, 'Q':16, 'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
form = input()
data = [int(input()) for _ in range(N)]
stack = []

for a in form:
    if a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        stack.append(data[alpha[a]])
    elif a in '+-*/':
        if len(stack) >= 2:
            if a == '*':
                current = stack.pop()
                previous = stack.pop()
                stack.append(current * previous)
            elif a == '/':
                current = stack.pop()
                previous = stack.pop()
                stack.append(previous/current)
            elif a == '+':
                current = stack.pop()
                previous = stack.pop()
                stack.append(current + previous)
            elif a == '-':
                current = stack.pop()
                previous = stack.pop()
                stack.append(previous - current)
result = stack[0]
print(format(result, ".2f"))