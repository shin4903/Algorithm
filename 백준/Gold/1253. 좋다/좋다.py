def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start < end:
        total = a[start] + a[end]
        if total == key:
            return True
        elif total > key:
            end -= 1
        elif total < key:
            start += 1
    return False

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
for i in range(N):
  arr2 = arr[:i] + arr[i+1:]
  if binarySearch(arr2, len(arr2), arr[i]):
      result += 1
print(result)