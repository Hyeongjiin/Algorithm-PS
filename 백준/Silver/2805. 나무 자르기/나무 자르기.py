import sys

def b_search(data, M, start, end):
    result = 0
    while start <= end:
        count = 0
        mid = (start + end) // 2
        for i in data:
            if i > mid:
                count += i - mid
        if count < M:
            end = mid - 1
        else:
            start = mid + 1
            result = mid
    return result
      
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
start = 0
end = 2 * max(data)
height = b_search(data, M, start, end)
print(height)