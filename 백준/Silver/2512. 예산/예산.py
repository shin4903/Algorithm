def binarySearch(n, m):
    result = 0
    idx = 0
    while idx < n:
        end = m // (n - idx)
        start = arr[idx]
        if start <= end:
            m -= start
            result = max(result, start)
        elif start > end:
            m -= end
            result = max(result, end)
            return result
        idx += 1


    return result

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
M = int(input())

if sum(arr) <= M:
    print(max(arr))
else:
    print(binarySearch(N, M))