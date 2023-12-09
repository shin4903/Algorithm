def check(i,j):
    nums = [1,2,3,4,5,6,7,8,9]
    for k in range(9):
        if arr[i][k] in nums:
            nums.remove(arr[i][k])
        if arr[k][j] in nums:
            nums.remove(arr[k][j])

    ni = i // 3 * 3
    nj = j // 3 * 3
    for i in range(ni, ni + 3):
        for j in range(nj, nj + 3):
            if arr[i][j] in nums:
                nums.remove(arr[i][j])

    return nums
flag = False
def back(s):
    global flag
    if flag:
        return
    if s == len(zero):
        for i in arr:
            result = ''
            for j in i:
                result += str(j)
            print(result)
        flag = True
        return
    x, y = zero[s]
    nums = check(x,y)
    for num in nums:
        arr[x][y] = num
        back(s+1)
        arr[x][y] = 0

arr = [list(map(int,input())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero.append([i,j])
back(0)